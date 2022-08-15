---
title: Establish temporary network connectivity
description: Establish temporary network connectivity
ms.date: 04/20/2017
---

# Establish temporary network connectivity


Telecommunication applications cannot initiate long-term connections. However, if you need temporary connectivity to a specific network, you can use the Mobile Broadband API as follows:

1.  Create an instance of [**IMbnConnectionManager**](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnectionmanager).

2.  Register to the [**IMbnConnectionEvents**](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnectionevents) connection point.

3.  Create an instance of [**IMbnInterfaceManager**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfacemanager).

4.  Get an [**IMbnInterface**](/windows/win32/api/mbnapi/nn-mbnapi-imbninterface) interface for the device by passing the account device ID into [**IMbnInterfaceManager::GetInterface**](/windows/win32/api/mbnapi/nf-mbnapi-imbninterfacemanager-getinterface). (For more info, see [Unlock a device](unlock-a-device.md).)

5.  Obtain an IMbnConnection interface for the device by calling [**IMbnConnectionManager::GetConnection**](/windows/win32/api/mbnapi/nf-mbnapi-imbnconnectionmanager-getconnection).

6.  Establish a connection by calling [**IMbnConnection::Connect**](/windows/win32/api/mbnapi/nf-mbnapi-imbnconnection-connect). The *connectionMode* parameter must be set to **MBN\_CONNECTION\_MODE\_TMP\_PROFILE**, and the *strProfile* parameter must be a mobile broadband profile description.

The results of the connect attempt are returned by using the [**IMbnConnectionEvents::OnConnectComplete**](/windows/win32/api/mbnapi/nf-mbnapi-imbnconnectionevents-onconnectcomplete) method. To disconnect when you are finished, invoke the [**IMbnConnection::Disconnect**](/windows/win32/api/mbnapi/nf-mbnapi-imbnconnection-disconnect) method. Status is returned by using [**IMbnConnectionEvents::OnDisconnectComplete**](/windows/win32/api/mbnapi/nf-mbnapi-imbnconnectionevents-ondisconnectcomplete).

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](./create-a-mobilebroadbandaccount-object.md)

 

