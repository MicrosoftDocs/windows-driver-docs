---
title: Bluetooth HFP DDI IOCTLs
description: Windows 8 introduces a set of I/O control codes (IOCTLs) as part of a DDI that allows the audio driver to work with the Hands-free profile (HFP) class driver, to operate a Bluetooth audio bypass connection.
ms.date: 11/28/2017
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

[**IOCTL\_BTHHFP\_DEVICE\_GET\_DESCRIPTOR**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_VOLUMEPROPERTYVALUES**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_volumepropertyvalues)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_KSNODETYPES**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_ksnodetypes)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CONTAINERID**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_containerid)

[**IOCTL\_BTHHFP\_DEVICE\_REQUEST\_CONNECT**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_request_connect)

[**IOCTL\_BTHHFP\_DEVICE\_REQUEST\_DISCONNECT**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_request_disconnect)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CONNECTION\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_connection_status_update)

[**IOCTL\_BTHHFP\_SPEAKER\_SET\_VOLUME**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_speaker_set_volume)

[**IOCTL\_BTHHFP\_SPEAKER\_GET\_VOLUME\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_speaker_get_volume_status_update)

[**IOCTL\_BTHHFP\_MIC\_SET\_VOLUME**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_mic_set_volume)

[**IOCTL\_BTHHFP\_MIC\_GET\_VOLUME\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_mic_get_volume_status_update)

[**IOCTL\_BTHHFP\_STREAM\_OPEN**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_open)

[**IOCTL\_BTHHFP\_STREAM\_CLOSE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_close)

[**IOCTL\_BTHHFP\_STREAM\_GET\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_stream_get_status_update)

Windows 8.1 has updated the set of IOCTLs by adding the following new ones:

[**IOCTL\_BTHHFP\_DEVICE\_GET\_DESCRIPTOR2**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_descriptor2)

[**IOCTL\_BTHHFP\_DEVICE\_GET\_NRECDISABLE\_STATUS\_UPDATE**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_nrecdisable_status_update)

Windows 10 has updated the set of IOCTLs by adding the following new one:

[**IOCTL\_BTHHFP\_DEVICE\_GET\_CODEC\_ID**](/windows-hardware/drivers/ddi/bthhfpddi/ni-bthhfpddi-ioctl_bthhfp_device_get_codec_id)

For information about the structures that work with these IOCTLs, see [Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md).

## <span id="related_topics"></span>Related topics


[Bluetooth HFP DDI Structures](bluetooth-hfp-ddi-structures.md)

 

