---
title: Bug Check 0x136 VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE
description: The VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE bug check has a value of 0x00000136 indicating an initialization failure while booting from a VHD. There is not enough free space to expand the VHD.
keywords: ["Bug Check 0x136 VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE", "VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- VHD_BOOT_HOST_VOLUME_NOT_ENOUGH_SPACE
api_type:
- NA
---

# Bug Check 0x136: VHD\_BOOT\_HOST\_VOLUME\_NOT\_ENOUGH\_SPACE


The VHD\_BOOT\_HOST\_VOLUME\_NOT\_ENOUGH\_SPACE bug check has a value of 0x00000136. This indicates that an initialization failure occurred while attempting to boot from a VHD. The volume that hosts the VHD does not have enough free space to expand the VHD.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).


## VHD\_BOOT\_HOST\_VOLUME\_NOT\_ENOUGH\_SPACE Parameters


| Parameter | Description                                 |
|-----------|---------------------------------------------|
| 1         | 0 : Unable to expand VHD file to full size. |
| 2         | NT Status Code                              |
| 3         | Reserved                                    |
| 4         | Reserved                                    |

 

 

 




