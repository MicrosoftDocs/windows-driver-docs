---
title: SCSI Driver
author: windows-driver-content
description: SCSI Driver
MS-HAID:
- 'WIA\_drv\_basic\_4076f288-5fc7-464e-b368-65e2dd5a79b2.xml'
- 'image.scsi\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e69e3ac6-6726-4f63-afdb-2da1255dde19
---

# SCSI Driver


## <a href="" id="ddk-scsi-driver-si"></a>


The kernel-mode still image driver for SCSI buses supports **ReadFile** by creating a command descriptor block (CDB) that includes a SCSI **Read** command. It supports **WriteFile** by creating a CDB that includes a SCSI **Write** command. User-mode minidrivers can specify customized CDBs by calling [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216). For more information, see [SCSI Still Image I/O Control Codes](https://msdn.microsoft.com/library/windows/hardware/ff548003). See the Microsoft Windows SDK documentation for descriptions of **ReadFile** and **WriteFile**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20SCSI%20Driver%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


