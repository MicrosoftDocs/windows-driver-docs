---
title: Initialization
description: Initialization
ms.assetid: 7d5ee1c7-df6c-4394-9ba7-819ee7e9397b
---

# Initialization


The LSI\_U3 Storport miniport driver's entry points are initialized in the DriverEntry routine. Other important initialization routines are LsiU3HWInitialize and LsiU3FindAdapter. In the latter, the driver's synchronization model is set to *StorSynchronizeFullDuplex*, which means the driver can receive new requests while it is completing previous requests. In other words, it may be simultaneously queuing up new requests from Storport while it is asynchronously completing previous requests.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Initialization%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




