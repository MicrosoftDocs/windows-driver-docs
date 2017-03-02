---
title: Handling Control Requests
---

# Handling Control Requests

NDIS 6.x Control Path

Three main types of control requests: query, set, method

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


Let’s use the same example as before (OID_GEN_INTERRUPT_MODERATION) and consider the following three cases:
1)	If the miniport registered a handler, then the registered handler will be used. In the code example of netvminikmdf, the default query handler will not be called if protocol issues OID_GEN_INTERRUPT_MODERATION to the miniport because miniport has a specialized handler for OID_GEN_INTERRUPT_MODERATION. In fact, netvminikmdf doesn’t even register a default query handler.
2)	If the miniport doesn’t register a handler, the default handler for that type of request will be used. In the code example of netvminikmdf, the miniport doesn’t register a special set handler for OID_GEN_INTERRUPT_MODERATION, thus the default set handler is used since netvminikmdf registered a default set handler.
3)	If neither specialized handler nor default handler is registered, the OID request would fail.

When the miniport configures the NET_REQUEST_QUEUE, I don’t think it has control over the sizeof* variables directly. So client driver doesn’t specify anything for that variable, the client driver would simply register 5 “set” handlers.

Since CX interacts with NDIS in the traditional way, EvtRequestDefault is used when the NDIS_REQUEST_TYPE doesn’t fall into the three known categories. For example, if protocol issues an OID request with NDIS_REQUEST_TYPE = NdisRequestGeneric1, CX would use EvtRequestDefault if the client driver registered one.

NETREQUESTQUEUE represents an OID Queue. NDIS Wdf client creates 2 NETREQUESTQUEUEs. One is for regular OIDs (sequential) and another one is for Direct OIDs (parallel).  
With the Queue it associates various event callbacks for different OIDs.  
* General Oid Handlers: 
o EvtDefaultSetData 
o EvtDefaultQueryData 
o EvtDefaultMethod 
o EvtDefault 
* Custom Handlers  
o NET_REQUEST_QUEUE_CONFIG_ADD_QUERY_DATA_HANDLER
