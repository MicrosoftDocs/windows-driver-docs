---
title: CODECAPI_AUDIO_ENCODER
description: Audio encoders use the support of this GUID to indicate they are an audio encoder.
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CODECAPI_AUDIO_ENCODER

Audio encoders use the support of this GUID (queried by the user-mode KsProperty BASICSUPPORT) to indicate they are an audio encoder.

| Get | Set | Target | Property descriptor type | Property value type |
|--|--|--|--|--|
| Yes | No | Filter | KSPROPERTY | BOOL |

The property value (operation data) is of type BOOL and specifies whether the minidriver supports audio encoding. A value of **TRUE** indicates that the minidriver supports audio encoding. The filter should not support this GUID if it is not an audio encoder.

## Requirements

**Headers:** Declared in *ksmedia.h*. Include *ksmedia.h*.

## See also

[**KSPROPERTY**](ksproperty-structure.md)
