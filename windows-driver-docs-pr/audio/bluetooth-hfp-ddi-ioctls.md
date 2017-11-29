---
title: Bluetooth HFP DDI IOCTLs
description: Windows 8 introduces a set of I/O control codes (IOCTLs) as part of a DDI that allows the audio driver to work with the Hands-free profile (HFP) class driver, to operate a Bluetooth audio bypass connection.
ms.assetid: 94B6F113-5130-4772-B8A0-5C9992501824
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bluetooth HFP DDI IOCTLs


Windows 8 introduces a set of I/O control codes (IOCTLs) as part of a DDI that allows the audio driver to work with the Hands-free profile (HFP) class driver, to operate a Bluetooth audio bypass connection.

Unless otherwise stated, the following is true for all the IOCTLs in this section:

-   If the request is successful, the Information member of the STATUS\_BLOCK structure is set to the size, in bytes, of the output buffer. Otherwise, the Information member is set to zero. The Status member is set to an NTSTATUS value.

-   All IOCTLS require IRQL &lt;= PASSIVE\_LEVEL.

-   The audio driver should use the IOCTLs with the IRP\_MJ\_DEVICE\_CONTROL request.

For most of the IOCTL function codes, the audio driver must initialize the FileObject pointer in the IO\_STACK\_LOCATION for the HFP driver when the audio driver initializes a device control IRP to send to the HFP driver. The audio driver typically retrieves the file object pointer by calling IoGetDeviceObjectPointer.

The audio driver will likely send many of these requests on an arbitrary thread (in other words, an “asynchronous” request). In these cases the audio driver will need to build the IRP itself using the IoAllocateIrp method, and set fields in the IRP directly rather than calling IoBuildDeviceIoControlRequest.

The following topics provide more details about these Windows 8 IOCTLs:

[**IOCTL\_BTHHFP\_DEVICE\_GET\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/dn265108)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_VOLUMEPROPERTYVALUES**](https://msdn.microsoft.com/library/windows/hardware/dn265113)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_KSNODETYPES**](https://msdn.microsoft.com/library/windows/hardware/dn265110)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CONTAINERID**](https://msdn.microsoft.com/library/windows/hardware/dn265107)

[**IOCTL\_BTHHFP\_DEVICE\_REQUEST\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/dn265114)

[**IOCTL\_BTHHFP\_DEVICE\_REQUEST\_DISCONNECT**](https://msdn.microsoft.com/library/windows/hardware/dn265115)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CONNECTION\_STATUS\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/dn265106)

[**IOCTL\_BTHHFP\_SPEAKER\_SET\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/dn265119)

[**IOCTL\_BTHHFP\_SPEAKER\_GET\_VOLUME\_STATUS\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/dn265118)

[**IOCTL\_BTHHFP\_MIC\_SET\_VOLUME**](https://msdn.microsoft.com/library/windows/hardware/dn265117)

[**IOCTL\_BTHHFP\_MIC\_GET\_VOLUME\_STATUS\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/dn265116)

[**IOCTL\_BTHHFP\_STREAM\_OPEN**](https://msdn.microsoft.com/library/windows/hardware/dn265122)

[**IOCTL\_BTHHFP\_STREAM\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/dn265120)

[**IOCTL\_BTHHFP\_STREAM\_GET\_STATUS\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/dn265121)

Windows 8.1 has updated the set of IOCTLs by adding the following new ones:

[**IOCTL\_BTHHFP\_DEVICE\_GET\_DESCRIPTOR2**](https://msdn.microsoft.com/library/windows/hardware/dn265109)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_NRECDISABLE\_STATUS\_UPDATE**](https://msdn.microsoft.com/library/windows/hardware/dn265112)

Windows 10 has updated the set of IOCTLs by adding the following new one:

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CODEC\_ID**](https://msdn.microsoft.com/library/windows/hardware/dn798965)

For information about the structures that work with these IOCTLs, see [Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md).

## <span id="related_topics"></span>Related topics


[Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Bluetooth%20HFP%20DDI%20IOCTLs%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





