---
title: Photo Sequence Mode
author: windows-driver-content
description: Photo sequence mode enables capturing a sequence of photos in response to a single photo click of the camera.
ms.assetid: 15F19FE1-6D09-4406-B096-E96D12BAF030
---

# Photo Sequence Mode


Photo sequence mode enables capturing a sequence of photos in response to a single photo click of the camera. In this mode, the capture system continuously sends buffers to the camera driver to capture the photos in a sequence. This mode also allows capturing photos from a time period prior to photo click.

## Photo sequence operation


A camera driver supports the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567582) control if is capable of sequencing photos. The capture pipeline starts a photo sequence by sending down a **KS\_VideoControlFlag\_StartPhotoSequenceCapture** trigger to the photo stream. At this point, the driver must start sending capture buffers. The capture pipeline will stop the photo sequence by sending down **KS\_VideoControlFlag\_StopPhotoSequenceCapture** to trigger the photo stream off. For each completed photo, a new buffer is sent down to the driver for it to capture frames into.

The capture pipeline has a configuration phase for the photo sequence mode during which it will configure the number of past frames needed for a particular photo sequence session. During the configuration phase, the driver must specify the maximum number of past photo frames it supports. Also, the driver will specify how many buffers are needed to support the required number of past frames.

The extended control, [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](https://msdn.microsoft.com/library/windows/hardware/dn567584), will pass down the actual time the user clicked the photo trigger in the camera application to take the photo sequence. Without this time the driver will not know which photo capture to start returning frames from when the **KS\_VideoControlFlag\_StartPhotoSequenceCapture** trigger arrives. With this control, the driver is expected to return the photo that is closest to the photo trigger time given.

## Frame count negotiation


The following sequence of operations sets the photo mode and frame count for the camera driver.

1.  An application calls an API to prepare the capture system and driver for a photo sequence capture.

2.  The capture system sends a calls the Photo Mode extended property request to the driver, [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567582) with KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE set in the flags, to start the transition of the driver to photo sequence mode.

    1.  The driver is given the requested history frame count from the application. Driver must return the history frame count it is capable of supporting along with the number of buffers needed for to hold history frames.

    2.  The driver must update the allocator requirements structure of the pin with the number of buffers by the photo sequence mode transition call using **KsEdit**.

    3.  The driver will change its internal state to photo sequence mode.

3.  The capture system will transition the pin to KSSTATE\_RUN and provide the driver with the number of buffers requested for photo sequence mode.

## Control support requirements


Support for the following extended controls is required for a camera driver to support photo sequence mode.

-   Photo Mode

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567582)

-   Photo Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOFRAMERATE**](https://msdn.microsoft.com/library/windows/hardware/dn567580)

-   Photo Maximum Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMAXFRAMERATE**](https://msdn.microsoft.com/library/windows/hardware/dn567581)

-   Photo Trigger Time

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](https://msdn.microsoft.com/library/windows/hardware/dn567584)

-   Photo Thumbnail

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL**](https://msdn.microsoft.com/library/windows/hardware/dn567583)

-   Maximum Video Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES**](https://msdn.microsoft.com/library/windows/hardware/dn567578)

-   Flash Mode (supporting KSCAMERA\_EXTENDEDPROP\_FLASH\_SINGLEFLASH capability)

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](https://msdn.microsoft.com/library/windows/hardware/dn567575)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Photo%20Sequence%20Mode%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


