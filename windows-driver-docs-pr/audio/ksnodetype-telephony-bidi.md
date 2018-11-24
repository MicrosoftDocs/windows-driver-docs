---
title: KSNODETYPE\_TELEPHONY\_BIDI
description: The KSNODETYPE\_TELEPHONY\_BIDI node represents both sides (bi-directional) of a phone call.
ms.assetid: 748AC39F-0C15-44A3-BF7B-109A1CB7D145
keywords: ["KSNODETYPE_TELEPHONY_BIDI Audio Devices"]
topic_type:
- apiref
api_name:
- KSNODETYPE_TELEPHONY_BIDI
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSNODETYPE\_TELEPHONY\_BIDI


The KSNODETYPE\_TELEPHONY\_BIDI node represents both sides (bi-directional) of a phone call.

If the device supports cellular telephony then a KSNODETYPE\_TELEPHONY\_BIDI endpoint for each Provider (executor) is required.

## <span id="CELLULAR_TELEPHONY__"></span><span id="cellular_telephony__"></span>CELLULAR TELEPHONY


The radio stack has a concept of Provider Id (Executor Id) and call type (packet/circuit) to connect the phone call instance to a specific hardware path.

The driver associates a provider Id to the wave filter. This provider Id will also be set on the associated cellular streaming endpoints. The provider Id for the wave filter must not change at runtime. The audio stack will query the provider Id from the driver by using [**KSPROPERTY\_TELEPHONY\_PROVIDERID**](ksproperty-telephony-providerid.md). After this, all the calls for that provider Id will be sent to the particular wave filter.

**STARTING AND ENDING CELLULAR CALLS**

Starting and stopping calls is done by sending [**KSPROPERTY\_TELEPHONY\_CALLCONTROL**](ksproperty-telephony-callcontrol.md) to the wave filter for the provider. This property will communicate call type (packet switched/circuit switched) and call control operation (Enable or Disable) to driver. Call type is ignored when the call control operation is Disable.

Once the call is Enabled, associated KSNODETYPE\_TELEPHONY\_BIDI’s jack state will be made Active by the driver and the call state will be updated to *TELEPHONY\_CALLSTATE\_ENABLED*. When the call is terminated, the endpoint's jack state will change to unplugged and the call state will be updated to *TELEPHONY\_CALLSTATE\_DISABLED*.

 

 





