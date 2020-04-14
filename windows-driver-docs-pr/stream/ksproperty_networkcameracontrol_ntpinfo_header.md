---
title: KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_HEADER (ksmedia.h)
description: Contains a NTP-specific payload that is used to set or disable an NTP server on a Onvif protocol camera.
ms.date: 04/14/2020
ms.localizationpriority: medium
---

# KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_HEADER structure

The **KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_HEADER** structure contains a NTP-specific payload that is used to set or disable an NTP server on a Onvif
protocol camera.

## Syntax

```cpp
typedef struct
{
  ULONG Size;
  KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_TYPE Type;
} KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_HEADER, *PKSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_HEADER;
```

## Members

### Size

The size of the NTP-specific payload.

### Type

Contains one of the values from the [KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_networkcameracontrol_ntpinfo_type) enumeration.

## Remarks

This command will be used to set or disable an NTP server on the Onvif protocol camera. The app can choose to configure the camera to use the same NTP server as is used by the local machine (for example, the Windows device that is controlling the camera.) It can also be used to configure the camera to use a custom NTP server.

The local PC's NTP server entry is found by parsing the registry value at SYSTEM\\CurrentControlSet\\Services\\W32Time\\Parameters\\. Apps can scan the space-separated registry value for the most optimal server to set on the camera.

## Requirements

| &nbsp; | &nbsp; |
| --- | --- |
| Header | ksmedia.h (include Ksmedia.h) |

## See also

[KSPROPERTY_NETWORKCAMERACONTROL_NTPINFO_TYPE](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_networkcameracontrol_ntpinfo_type)

[KSPROPERTY_NETWORKCAMERACONTROL_PROPERTY](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ne-ksmedia-ksproperty_networkcameracontrol_property)
