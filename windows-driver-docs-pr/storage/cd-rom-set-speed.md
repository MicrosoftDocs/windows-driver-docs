---
title: CD-ROM Set Speed
description: CD-ROM Set Speed
ms.assetid: 25a46b23-f823-4fc7-a370-cab1c9418a94
keywords:
- CD-ROM drivers WDK storage
- storage CD-ROM drivers WDK
- power management WDK CD-ROM
- speed WDK CD-ROM
- battery power WDK CD-ROM
- playback speed WDK CD-ROM
- spindle speed WDK CD-ROM
- SET CD SPEED
- SET STREAMING
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CD-ROM Set Speed


It is often convenient to spin CDs at a speed that is less than the optimal spindle speed that the CD-ROM drive allows. For example, in portable computers, CD-ROM drives that spin at high speed drain the battery very quickly. You can set the CD-ROM drive to a low speed to conserve battery power.

Some computers do not require CD-ROM drives to operate at high speeds. For example, CD-ROM drives in media-center computers primarily perform operations, such as audio playback, that do not require speeds above 1X. CD-ROM drives that spin at, for example, 16X during playback, when a speed of only 1X is required, can produce loud noise that leads to a bad user experience.

Version 2 of the *SCSI-3 Multimedia Commands* (MMC) specification defines two commands for setting the CD-ROM speed: SET CD SPEED and SET STREAMING. In Windows Vista, applications can instruct the CD-ROM class driver to issue one of these two commands by sending an [**IOCTL\_CDROM\_SET\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff559381) request to the class driver.

To send the SET CD SPEED command to a CD-ROM device, the caller specifies a request type of **CdromSetSpeed** in the **RequestType** member of [**CDROM\_SET\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff551368), on input to IOCTL\_CDROM\_SET\_SPEED.

To send a SET STREAMING command to the device, the caller specifies a request type of **CdromSetStreaming** in the **RequestType** member of [**CDROM\_SET\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff551369), on input to IOCTL\_CDROM\_SET\_SPEED.

If an application changes the spindle speed with a SET CD SPEED command, the device automatically returns to its default speed when the media is changed. If an application changes the spindle speed with a SET STREAMING command, a change of media does not affect the speed, unless the caller specifies a value of **FALSE** in the **Persistent** member of the CDROM\_SET\_STREAMING structure.

The SET STREAMING request works only on an MMC-compliant device. If an application sends this request to a device that is not MMC-compliant, the CD-ROM class driver will fail the request.

 

 




