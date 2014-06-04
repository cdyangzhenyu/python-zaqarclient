# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
import requests as prequest

from marconiclient.tests import base
from marconiclient.tests.transport import api
from marconiclient.transport import http
from marconiclient.transport import request


class TestHttpTransport(base.TestBase):

    """Tests for the HTTP transport."""

    def setUp(self):
        super(TestHttpTransport, self).setUp()
        self.api = api.FakeApi()
        self.transport = http.HttpTransport(self.conf)

    def test_basic_send(self):
        params = {'name': 'Test',
                  'address': 'Outer space'}
        req = request.Request('http://example.org/',
                              operation='test_operation',
                              params=params)

        with mock.patch.object(self.transport.client, 'request',
                               autospec=True) as request_method:

            resp = prequest.Response()
            request_method.return_value = resp

            # NOTE(flaper87): Bypass the API
            # loading step by setting the _api
            # attribute
            req._api = self.api
            self.transport.send(req)

            final_url = 'http://example.org/v1/test/Test'
            final_params = {'address': 'Outer space'}
            final_headers = {'content-type': 'application/json'}

            request_method.assert_called_with('GET', url=final_url,
                                              params=final_params,
                                              headers=final_headers,
                                              data=None)

    def test_send_without_api(self):
        params = {'name': 'Test',
                  'address': 'Outer space'}
        req = request.Request('http://example.org/',
                              operation='test_operation',
                              params=params)

        with mock.patch.object(self.transport.client, 'request',
                               autospec=True) as request_method:

            resp = prequest.Response()
            request_method.return_value = resp
            self.transport.send(req)

            final_url = 'http://example.org/'
            final_headers = {'content-type': 'application/json'}

            request_method.assert_called_with('GET', url=final_url,
                                              params=params,
                                              headers=final_headers,
                                              data=None)

    def test_error_handling(self):
        params = {'name': 'Opportunity',
                  'address': 'NASA'}
        req = request.Request('http://example.org/',
                              operation='test_operation',
                              params=params)

        with mock.patch.object(self.transport.client, 'request',
                               autospec=True) as request_method:

            exception_iterator = self.transport.http_to_marconi.items()

            for response_code, exception in exception_iterator:

                resp = prequest.Response()
                resp.status_code = response_code
                request_method.return_value = resp
                self.assertRaises(exception, lambda: self.transport.send(req))
