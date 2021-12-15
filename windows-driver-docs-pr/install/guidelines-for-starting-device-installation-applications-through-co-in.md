---
title: Starting Device Installation Applications through Co-installers
description: Guidelines for Starting Device Installation Applications through Co-installers
ms.date: 04/20/2017
---

# Guidelines for Starting Device Installation Applications through Co-installers


The following guidelines must be followed for co-installers which supply finish-install actions (Windows Vista and later versions of Windows) to start *device installation applications*:

-   A co-installer must not exit from its finish-install pages or finish-install action until the device installation application has finished. If a co-installer exits early and another driver requires a restart, Windows might restart the computer before the application has completed.

-   A co-installer should first look for the device installation application on the distribution medium and, if the application is present, silently begin the installation process.

    If the distribution medium is not present, the co-installer should offer the user the choice of either inserting a medium or downloading the device installation application from the Internet. If the user chooses to insert the medium, the co-installer should detect the new media notification, silently exit, and allow the medium's AutoRun process to start the device installation application.

    A co-installer can detect the new media by listening for a WM_DEVICECHANGED/DBT_DEVICEARRIVAL message with dbch_devicetype set to DBT_DEVTYP_VOLUME and dbcv_flags set to DBTF_MEDIA.

    For more information, see [Detecting Media Insertion or Removal](/windows/win32/devio/detecting-media-insertion-or-removal).

-   A co-installer should never assume that the distribution media is available during installation. For example, a co-installer should never use the %1% DirId to find the media from within the co-installer.

    In Windows Vista and later versions of Windows, the co-installers are invoked after they are copied to the driver store. By this time, the distribution media might are removed, which is why it is important to avoid prompting the user for the medium. For example, suppose that a user performs a [software-first installation](software-first-installation.md), removes the distribution medium, and then plugs in the device. The co-installer is invoked only when the user plugs in the device for the first time.

-   If a co-installer starts Windows Internet Explorer to download the device installation application, it must start it in Protected Mode, which has features that protect users against malicious code.

    For more information about starting Internet Explorer in Protected Mode, see [Understanding and Working in Protected Mode Internet Explorer](/previous-versions/windows/internet-explorer/ie-developer/).

For more information about co-installers, see [Writing a Co-installer](writing-a-co-installer.md).

 

