---
title: TAEF Error Codes
description: TAEF Error Codes
ms.assetid: E42AF880-12DA-42b7-AB6D-90011BD7E548
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TAEF Error Codes


TAEF can encounter errors for a variety of reasons, such as being unable to connect to a machine for cross machine execution or receiving invalid values for well-known test metadata. When errors occur, TAEF shows an error message and often an HRESULT value associated with the error. Most of the HRESULT values are [well-known system error codes](http://msdn.microsoft.com/library/ms681381.aspx), but TAEF will sometimes show custom error codes.

## <span id="Custom_TAEF_HRESULT_Values"></span><span id="custom_taef_hresult_values"></span><span id="CUSTOM_TAEF_HRESULT_VALUES"></span>Custom TAEF HRESULT Values


TAEF's custom HRESULT values will be documented in the table below as they are added. Currently, there is only one TAEF-specific HRESULT value.

| HRESULT                             | Value      | Description                                                                                                                                                                                                                                    |
|-------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TAEF\_E\_INVALID\_TEST\_ENVIRONMENT | 0x81A40001 | A TAEF test requested an invalid test environment via its metadata. Examples of metadata that affect the test environment include [RunAs](runas.md), [ThreadingModel](threading-models.md), and [ActivationContext](activation-context.md). |

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20TAEF%20Error%20Codes%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




