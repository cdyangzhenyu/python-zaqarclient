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


from marconiclient.tests.queues import queues
from marconiclient.transport import http


class QueuesV1QueueHttpUnitTest(queues.QueuesV1QueueUnitTest):

    transport_cls = http.HttpTransport
    url = 'http://127.0.0.1:8888/v1'
    version = 1