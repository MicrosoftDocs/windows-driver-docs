---
title: Establish temporary network connectivity
description: Establish temporary network connectivity
ms.assetid: 5ee9d1ab-cc6f-4262-b2b0-e8b0b0c0c1d3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Establish temporary network connectivity


Telecommunication applications cannot initiate long-term connections. However, if you need temporary connectivity to a specific network, you can use the Mobile Broadband API as follows:

1.  Create an instance of [**IMbnConnectionManager**](https://msdn.microsoft.com/library/windows/desktop/dd430380).

2.  Register to the [**IMbnConnectionEvents**](https://msdn.microsoft.com/library/windows/desktop/dd430375) connection point.

3.  Create an instance of [**IMbnInterfaceManager**](https://msdn.microsoft.com/library/windows/desktop/dd430416).

4.  Get an [**IMbnInterface**](https://msdn.microsoft.com/library/windows/desktop/dd430406) interface for the device by passing the account device ID into [**IMbnInterfaceManager::GetInterface**](https://msdn.microsoft.com/library/windows/desktop/dd430420). (For more info, see [Unlock a device](unlock-a-device.md).)

5.  Obtain an IMbnConnection interface for the device by calling [**IMbnConnectionManager::GetConnection**](https://msdn.microsoft.com/library/windows/desktop/dd430384).

6.  Establish a connection by calling [**IMbnConnection::Connect**](https://msdn.microsoft.com/library/windows/desktop/dd430399). The *connectionMode* parameter must be set to **MBN\_CONNECTION\_MODE\_TMP\_PROFILE**, and the *strProfile* parameter must be a mobile broadband profile description.

The results of the connect attempt are returned by using the [**IMbnConnectionEvents::OnConnectComplete**](https://msdn.microsoft.com/library/windows/desktop/dd430376) method. To disconnect when you are finished, invoke the [**IMbnConnection::Disconnect**](https://msdn.microsoft.com/library/windows/desktop/dd430401) method. Status is returned by using [**IMbnConnectionEvents::OnDisconnectComplete**](https://msdn.microsoft.com/library/windows/desktop/dd430378).

## <span id="related_topics"></span>Related topics


[Common tasks for mobile broadband Windows Runtime APIs](common-tasks-for-mobile-broadband-windows-runtime-apis.md)

 

 






