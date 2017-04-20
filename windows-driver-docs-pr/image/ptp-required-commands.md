---
title: PTP Required Commands
author: windows-driver-content
description: PTP Required Commands
ms.assetid: 98f4be09-0f13-45a1-b28a-c027e57c0dd7
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PTP Required Commands


## <a href="" id="ddk-ptp-required-commands-si"></a>


PTP drivers must support commands marked as mandatory in the *Conformance Section* (chapter 14) of the PIMA15740 specification. The only exception is that the **GetNumObjects** command is not used. In other words, if a device is compliant with the PIMA15740 specification, it will work with Microsoft Windows Me, Windows XP, and later.

The full list of required PTP commands is:

0x1001 **GetDeviceInfo**

0x1002 **OpenSession**

0x1003 **CloseSession**

0x1004 **GetStorageIDs**

0x1005 **GetStorageInfo**

0x1007 **GetObjectHandles**

0x1008 **GetObjectInfo**

0x1009 **GetObject**

0x100A **GetThumb**

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20PTP%20Required%20Commands%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


