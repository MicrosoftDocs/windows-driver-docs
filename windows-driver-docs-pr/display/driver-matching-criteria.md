---
title: Driver matching criteria
description: This topic describes the elements that are used to choose the best match on a driver.
ms.assetid: C41549AE-3FE0-44E8-9D45-1ED1124D010B
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Driver matching criteria


This topic describes the elements that are used to choose the best match on a driver.

The following elements are used to choose the best match on a driver. They are listed in order from most significant to least significant:

1.  Signature
    1.  Signed
    2.  Unsigned

2.  Scope
    1.  Specific
    2.  Basic - DNF\_BASIC\_DRIVER

3.  Signature score
    1.  Within signed
        1.  \#define SIGNERSCORE\_LOGO\_PREMIUM 0x0D000001
        2.  \#define SIGNERSCORE\_LOGO\_STANDARD 0x0D000002
        3.  \#define SIGNERSCORE\_INBOX 0x0D000003
        4.  \#define SIGNERSCORE\_UNCLASSIFIED 0x0D000004 // UNCLASSIFIED == INBOX == STANDARD == PREMIUM when the SIGNERSCORE\_MASK filter is applied
        5.  \#define SIGNERSCORE\_WHQL 0x0D000005 // base WHQL.
        6.  \#define SIGNERSCORE\_AUTHENTICODE 0x0F000000

    2.  Within unsigned
        1.  \#define SIGNERSCORE\_UNSIGNED 0x80000000
        2.  \#define SIGNERSCORE\_W9X\_SUSPECT 0xC0000000
        3.  \#define SIGNERSCORE\_UNKNOWN 0xFF000000

4.  Feature Score, for display
    1.  Windows 8 WHQL E0
    2.  Windows 8 Pre-Release Driver E3
    3.  Windows 7 WHQL E6
    4.  Windows 7 Inbox EC
    5.  Windows Vista WHQL F6
    6.  Windows Vista Inbox F8
    7.  Microsoft Basic Display Driver FB
    8.  XDDM 3rd party FC (Not used in Windows 8)
    9.  XDDM Inbox in Windows Vista FD (Not used in Windows 8)
    10. VGA FE (Not used in Windows 8)
    11. Default or No Score FF
    12. Unsigned drivers FF
    13. No Feature score FF

5.  Match type (INF matches are listed under the models section as Description=Install Section, HWID, CompatID. With 0 or 1 HW IDs and 0 or more CompatIDs)
    1.  Device HardwareID == INF HardwareID
    2.  Device HardwareID == INF CompatID
    3.  Device CompatID == INF HardwareID
    4.  Device CompatID == INF CompatID

6.  Match rank: priority of match within list of matches from device
7.  Driver date
8.  Driver version number

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Driver%20matching%20criteria%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




