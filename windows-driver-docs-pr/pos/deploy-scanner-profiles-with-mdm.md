---
title: Deploy barcode scanner profiles with MDM
author: windows-driver-content
description: Barcode scanner profiles can be deployed with an MDM server.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 99ED3BD8-022C-40C2-9C65-F599186548FE
---

# Deploy barcode scanner profiles with MDM


**Note**  This feature requires Windows 10 Mobile or later.

 

Barcode scanner profiles can be deployed with an MDM server. To deploy the profiles, use *OemProfile* in the [EnterpriseExtFileSystem CSP](https://msdn.microsoft.com/library/windows/hardware/mt157025) to place them into the \\Data\\SharedData\\OEM\\Public\\Profile folder. These scanner profiles can then be used by driver manufacturers to configure settings that are not exposed through the API surface.

Microsoft does not define the specifics of a scanner profile or how to implement them.

## Related topics
[EnterpriseExtFileSystem CSP](https://msdn.microsoft.com/library/windows/hardware/mt157025)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bpos\pos%5D:%20Deploy%20barcode%20scanner%20profiles%20with%20MDM%20%20RELEASE:%20%289/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


