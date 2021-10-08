---
title: CODECAPI_VIDEO_ENCODER
description: Video encoders use the support of this GUID to indicate they are a video encoder.
ms.date: 10/08/2021
ms.localizationpriority: medium
---

# CODECAPI_VIDEO_ENCODER

Video encoders use the support of this GUID (queried by the user-mode KsProperty BASICSUPPORT) to indicate they are a video encoder.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | BOOL |

The property value (operation data) is of type BOOL and specifies whether the minidriver supports video encoding. A value of **TRUE** indicates that the minidriver supports video encoding. The filter should not support this GUID if it is not a video encoder.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)
