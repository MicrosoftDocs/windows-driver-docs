---
title: Photo Sequence Mode
description: Photo sequence mode enables capturing a sequence of photos in response to a single photo click of the camera.
ms.date: 04/20/2017
---

# Photo Sequence Mode


Photo sequence mode enables capturing a sequence of photos in response to a single photo click of the camera. In this mode, the capture system continuously sends buffers to the camera driver to capture the photos in a sequence. This mode also allows capturing photos from a time period prior to photo click.

## Photo sequence operation


A camera driver supports the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](./ksproperty-cameracontrol-extended-photomode.md) control if is capable of sequencing photos. The capture pipeline starts a photo sequence by sending down a **KS\_VideoControlFlag\_StartPhotoSequenceCapture** trigger to the photo stream. At this point, the driver must start sending capture buffers. The capture pipeline will stop the photo sequence by sending down **KS\_VideoControlFlag\_StopPhotoSequenceCapture** to trigger the photo stream off. For each completed photo, a new buffer is sent down to the driver for it to capture frames into.

The capture pipeline has a configuration phase for the photo sequence mode during which it will configure the number of past frames needed for a particular photo sequence session. During the configuration phase, the driver must specify the maximum number of past photo frames it supports. Also, the driver will specify how many buffers are needed to support the required number of past frames.

The extended control, [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](./ksproperty-cameracontrol-extended-phototriggertime.md), will pass down the actual time the user clicked the photo trigger in the camera application to take the photo sequence. Without this time the driver will not know which photo capture to start returning frames from when the **KS\_VideoControlFlag\_StartPhotoSequenceCapture** trigger arrives. With this control, the driver is expected to return the photo that is closest to the photo trigger time given.

## Frame count negotiation


The following sequence of operations sets the photo mode and frame count for the camera driver.

1.  An application calls an API to prepare the capture system and driver for a photo sequence capture.

2.  The capture system sends a calls the Photo Mode extended property request to the driver, [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](./ksproperty-cameracontrol-extended-photomode.md) with KSCAMERA\_EXTENDEDPROP\_PHOTOMODE\_SEQUENCE set in the flags, to start the transition of the driver to photo sequence mode.

    1.  The driver is given the requested history frame count from the application. Driver must return the history frame count it is capable of supporting along with the number of buffers needed for to hold history frames.

    2.  The driver must update the allocator requirements structure of the pin with the number of buffers by the photo sequence mode transition call using **KsEdit**.

    3.  The driver will change its internal state to photo sequence mode.

3.  The capture system will transition the pin to KSSTATE\_RUN and provide the driver with the number of buffers requested for photo sequence mode.

## Control support requirements


Support for the following extended controls is required for a camera driver to support photo sequence mode.

-   Photo Mode

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMODE**](./ksproperty-cameracontrol-extended-photomode.md)

-   Photo Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOFRAMERATE**](./ksproperty-cameracontrol-extended-photoframerate.md)

-   Photo Maximum Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOMAXFRAMERATE**](./ksproperty-cameracontrol-extended-photomaxframerate.md)

-   Photo Trigger Time

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTRIGGERTIME**](./ksproperty-cameracontrol-extended-phototriggertime.md)

-   Photo Thumbnail

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOTHUMBNAIL**](./ksproperty-cameracontrol-extended-photothumbnail.md)

-   Maximum Video Frame Rate

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_MAXVIDFPS\_PHOTORES**](./ksproperty-cameracontrol-extended-maxvidfps-photores.md)

-   Flash Mode (supporting KSCAMERA\_EXTENDEDPROP\_FLASH\_SINGLEFLASH capability)

    Control: [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FLASHMODE**](./ksproperty-cameracontrol-extended-flashmode.md)

 

