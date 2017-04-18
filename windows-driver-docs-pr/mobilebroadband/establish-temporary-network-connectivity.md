---
title: Establish temporary network connectivity
description: Establish temporary network connectivity
ms.assetid: 5ee9d1ab-cc6f-4262-b2b0-e8b0b0c0c1d3
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Establish%20temporary%20network%20connectivity%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





