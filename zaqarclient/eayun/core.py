# Copyright (c) 2017 Eayun, Inc.
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

"""
This module defines a lower level API for v2. This level of the
API is responsible for packing up the final request, sending it to the server
and handling asynchronous requests.

Functions present in this module assume that:

    1. The transport instance is ready to `send` the
    request to the server.

    2. Transport instance holds the conf instance to use for this
    request.
"""

import json

from zaqarclient.queues.v2 import core

queue_create = core.queue_create
queue_get = core.queue_get
queue_update = core.queue_update
queue_delete = core.queue_delete
queue_list = core.queue_list
queue_purge = core.queue_purge


def queue_get_monitor(transport, request, queue_name):
    """Gets a queue monitor data

    :param transport: Transport instance to use
    :type transport: `transport.base.Transport`
    :param request: Request instance ready to be sent.
    :type request: `transport.request.Request`
    :param queue_name: Queue reference name.
    :type queue_name: `six.text_type`

    """

    request.operation = 'queue_get_monitor'
    request.params['queue_name'] = queue_name

    resp = transport.send(request)
    return resp.deserialized_content


def topic_list(transport, request, callback=None, **kwargs):
    """Gets a list of topics

    :param transport: Transport instance to use
    :type transport: `transport.base.Transport`
    :param request: Request instance ready to be sent.
    :type request: `transport.request.Request`
    :param callback: Optional callable to use as callback.
        If specified, this request will be sent asynchronously.
        (IGNORED UNTIL ASYNC SUPPORT IS COMPLETE)
    :type callback: Callable object.
    :param kwargs: Optional arguments for this operation.
        - marker: Where to start getting topics from.
        - limit: Maximum number of queues to get.
    """

    request.operation = 'topic_list'

    request.params.update(kwargs)

    resp = transport.send(request)

    if not resp.content:
        return {'links': [], 'topics': []}

    return resp.deserialized_content


def topic_create(transport, request, name,
                 metadata=None, callback=None):
    """Creates a topic

    :param transport: Transport instance to use
    :type transport: `transport.base.Transport`
    :param request: Request instance ready to be sent.
    :type request: `transport.request.Request`
    :param name: topic reference name.
    :type name: `six.text_type`
    :param metadata: topic's metadata object. (>=v1.1)
    :type metadata: `dict`
    :param callback: Optional callable to use as callback.
        If specified, this request will be sent asynchronously.
        (IGNORED UNTIL ASYNC SUPPORT IS COMPLETE)
    :type callback: Callable object.
    """

    request.operation = 'topic_create'
    request.params['topic_name'] = name
    request.content = metadata and json.dumps(metadata)

    resp = transport.send(request)
    return resp.deserialized_content


def topic_get(transport, request, name, callback=None):
    """Retrieve a topic."""
    request.operation = 'topic_get'
    request.params['topic_name'] = name

    resp = transport.send(request)
    return resp.deserialized_content


def topic_delete(transport, request, name, callback=None):
    """Deletes topic."""
    request.operation = 'topic_delete'
    request.params['topic_name'] = name

    resp = transport.send(request)
    return resp.deserialized_content


def topic_get_monitor(transport, request, topic_name):
    """Gets a topic monitor data

    :param transport: Transport instance to use
    :type transport: `transport.base.Transport`
    :param request: Request instance ready to be sent.
    :type request: `transport.request.Request`
    :param topic_name: Topic reference name.
    :type topic_name: `six.text_type`

    """

    request.operation = 'topic_get_monitor'
    request.params['topic_name'] = topic_name

    resp = transport.send(request)
    return resp.deserialized_content


def topic_update(transport, request, name, metadata, callback=None):
    """Updates a topic's metadata using PATCH for API v2

    :param transport: Transport instance to use
    :type transport: `transport.base.Transport`
    :param request: Request instance ready to be sent.
    :type request: `transport.request.Request`
    :param name: Topic reference name.
    :type name: `six.text_type`
    :param metadata: Topic's metadata object.
    :type metadata: `list`
    :param callback: Optional callable to use as callback.
        If specified, this request will be sent asynchronously.
        (IGNORED UNTIL ASYNC SUPPORT IS COMPLETE)
    :type callback: Callable object.
    """

    request.operation = 'topic_update'
    request.params['topic_name'] = name
    request.content = json.dumps(metadata)

    resp = transport.send(request)
    return resp.deserialized_content
