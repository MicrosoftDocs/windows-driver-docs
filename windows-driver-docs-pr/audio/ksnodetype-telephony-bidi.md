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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20KSNODETYPE_TELEPHONY_BIDI%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




