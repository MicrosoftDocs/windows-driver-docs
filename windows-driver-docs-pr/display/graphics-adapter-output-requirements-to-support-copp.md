---
title: Graphics Adapter Output Requirements to Support COPP
description: Graphics Adapter Output Requirements to Support COPP
ms.assetid: e557487d-dba5-4185-9c35-da3185c291f6
keywords: ["copy protection WDK COPP , graphics adapter output requirements", "video copy protection WDK COPP , graphics adapter output requirements", "COPP WDK DirectX VA , graphics adapter output requirements", "protected video WDK COPP , graphics adapter output requirements", "graphics adapter output requirements WDK COPP"]
---

# Graphics Adapter Output Requirements to Support COPP


## <span id="ddk_display_adapter_output_requirements_to_support_copp_gg"></span><span id="DDK_DISPLAY_ADAPTER_OUTPUT_REQUIREMENTS_TO_SUPPORT_COPP_GG"></span>


**This section applies only to Windows Server 2003 SP1 and later, and Windows XP SP2 and later.**

To support COPP, the physical output connector of the graphics adapter must perform the following tasks:

<span id="Protect_key_information"></span><span id="protect_key_information"></span><span id="PROTECT_KEY_INFORMATION"></span>Protect key information  
A certified output must protect key information that was issued to the output upon certification.

<span id="Restrict_unauthorized_components_from_accessing_secure_content"></span><span id="restrict_unauthorized_components_from_accessing_secure_content"></span><span id="RESTRICT_UNAUTHORIZED_COMPONENTS_FROM_ACCESSING_SECURE_CONTENT"></span>Restrict unauthorized components from accessing secure content  
A certified output must prevent unauthorized software or hardware components from accessing content sent through a COPP secure channel. The certified output should only permit COPP commands to operate on data received through the COPP secure channel.

<span id="Switch_to_a_failure_mode_if_the_output_fails"></span><span id="switch_to_a_failure_mode_if_the_output_fails"></span><span id="SWITCH_TO_A_FAILURE_MODE_IF_THE_OUTPUT_FAILS"></span>Switch to a failure mode if the output fails  
If the certified output can no longer enforce the configuration profile specified at configuration time, then the output should cease decrypting incoming content and should send a status message to the application. The status message should indicate that the output can no longer perform as configured.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Graphics%20Adapter%20Output%20Requirements%20to%20Support%20COPP%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




