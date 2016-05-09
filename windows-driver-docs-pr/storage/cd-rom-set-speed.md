---
title: CD-ROM Set Speed
author: windows-driver-content
description: CD-ROM Set Speed
ms.assetid: 25a46b23-f823-4fc7-a370-cab1c9418a94
keywords: ["CD-ROM drivers WDK storage", "storage CD-ROM drivers WDK", "power management WDK CD-ROM", "speed WDK CD-ROM", "battery power WDK CD-ROM", "playback speed WDK CD-ROM", "spindle speed WDK CD-ROM", "SET CD SPEED", "SET STREAMING"]
---

# CD-ROM Set Speed


It is often convenient to spin CDs at a speed that is less than the optimal spindle speed that the CD-ROM drive allows. For example, in portable computers, CD-ROM drives that spin at high speed drain the battery very quickly. You can set the CD-ROM drive to a low speed to conserve battery power.

Some computers do not require CD-ROM drives to operate at high speeds. For example, CD-ROM drives in media-center computers primarily perform operations, such as audio playback, that do not require speeds above 1X. CD-ROM drives that spin at, for example, 16X during playback, when a speed of only 1X is required, can produce loud noise that leads to a bad user experience.

Version 2 of the *SCSI-3 Multimedia Commands* (MMC) specification defines two commands for setting the CD-ROM speed: SET CD SPEED and SET STREAMING. In Windows Vista, applications can instruct the CD-ROM class driver to issue one of these two commands by sending an [**IOCTL\_CDROM\_SET\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff559381) request to the class driver.

To send the SET CD SPEED command to a CD-ROM device, the caller specifies a request type of **CdromSetSpeed** in the **RequestType** member of [**CDROM\_SET\_SPEED**](https://msdn.microsoft.com/library/windows/hardware/ff551368), on input to IOCTL\_CDROM\_SET\_SPEED.

To send a SET STREAMING command to the device, the caller specifies a request type of **CdromSetStreaming** in the **RequestType** member of [**CDROM\_SET\_STREAMING**](https://msdn.microsoft.com/library/windows/hardware/ff551369), on input to IOCTL\_CDROM\_SET\_SPEED.

If an application changes the spindle speed with a SET CD SPEED command, the device automatically returns to its default speed when the media is changed. If an application changes the spindle speed with a SET STREAMING command, a change of media does not affect the speed, unless the caller specifies a value of **FALSE** in the **Persistent** member of the CDROM\_SET\_STREAMING structure.

The SET STREAMING request works only on an MMC-compliant device. If an application sends this request to a device that is not MMC-compliant, the CD-ROM class driver will fail the request.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20CD-ROM%20Set%20Speed%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


