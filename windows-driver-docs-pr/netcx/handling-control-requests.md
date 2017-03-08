---
title: Handling Control Requests
---

# Handling Control Requests

NDIS 6.x Control Path

To complete: mark the OID something other than NDIS_STATUS_PENDING, or call *RequestComplete.


OIDs are still the way to deliver most control messages
Few exceptions: for example OID_PM_PARAMETERS, OID_PNP_SET_POWER (see porting guide)
The two categories of OIDs are preserved (Serial and Direct)

NETREQUESTQUEUE (Parents to a NETADAPTER)
NETREQUEST (Parents to a NETREQUESTQUEUE) represents a control request
Client driver creates request queues during PnP add
Request queues are tied to a specific adapter

NETREQUESTQUEUE modeled to resemble WDFQUEUEs (look at the def)

Reminder: A NETREQUESTQUEUE can start to receive NETREQUESTs as soon as EvtDevicePrepareHardware is finished up until EvtDeviceReleaseHardware

For each of the three main request types (query data, set data, and method), the client driver can provide a single default handler for that request type, or one or more individual handlers for OID requests of that type, or both.

For example, for requests with `NDIS_REQUEST_TYPE=NdisRequestQueryInformation`, the handlers are:

* [*EVT_NET_REQUEST_DEFAULT_QUERY_DATA*](evt-net-request-default-query-data.md)
* [*EVT_NET_REQUEST_QUERY_DATA*](evt-net-request-query-data.md)

If a specialized OID handler is provided, NetAdapter calls that handler; otherwise, NetAdapterCx calls the default handler for the request type.

To register it, use... from...
<!--see sample code-->

For requests of type other than the three main ones, the client driver can provide [**EVT_NET_REQUEST_DEFAULT callback function**](evt-net-request-default.md)

For example, if protocol issues an OID request with NDIS_REQUEST_TYPE = NdisRequestGeneric1, CX would use EvtRequestDefault if the client driver registered one.

NETREQUESTQUEUE represents an OID Queue. NDIS Wdf client creates 2 NETREQUESTQUEUEs. One is for regular OIDs (sequential) and another one is for Direct OIDs (parallel).  
With the Queue it associates various event callbacks for different OIDs.  
* General Oid Handlers: 
o EvtDefaultSetData 
o EvtDefaultQueryData 
o EvtDefaultMethod 
o EvtDefault 
* Custom Handlers  
o NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER
