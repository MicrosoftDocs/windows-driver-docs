---
title: Bluetooth HFP DDI IOCTLs
description: Windows 8 introduces a set of I/O control codes (IOCTLs) as part of a DDI that allows the audio driver to work with the Hands-free profile (HFP) class driver, to operate a Bluetooth audio bypass connection.
ms.assetid: 94B6F113-5130-4772-B8A0-5C9992501824
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 






