---
title: Approving the Sdv-map.h File
description: Approving the Sdv-map.h File
ms.assetid: eb192eb2-7a2c-47eb-846e-3d641d5046a8
keywords: ["Sdv-map.h WDK Static Driver Verifier , approving", "approving Sdv-map.h"]
---

# Approving the Sdv-map.h File


The Sdv-map.h file includes a line of text that tells SDV that you have approved the file, presumably after examining the file and correcting any errors. When it is created, the Sdv-map.h file includes the phrase: "Approved=false."

### <span id="to_approve_an_sdv_map_h_file"></span><span id="TO_APPROVE_AN_SDV_MAP_H_FILE"></span>To approve an Sdv-map.h file

1.  Open the Sdv-map.h file in a text editor, such as Notepad. SDV creates the Sdv-map.h file in the driver's sources directory. (It is the local directory for a verification.)

2.  Change **//Approved=false** to **//Approved=true**.

### <span id="when_you_should_approve_a_sdv_map_h_file"></span><span id="WHEN_YOU_SHOULD_APPROVE_A_SDV_MAP_H_FILE"></span>When you should approve a Sdv-map.h file

The Sdv-map.h is correct and complete when SDV:

-   Found all of the entry points that it uses.

-   Has associated the entry points with the correct function role types.

### <span id="when_you_should_correct_a_sdv_map_h_file"></span><span id="WHEN_YOU_SHOULD_CORRECT_A_SDV_MAP_H_FILE"></span>When you should correct a Sdv-map.h file

The Sdv-map.h file is incorrect or incomplete when SDV:

-   Has not detected any entry points in the driver, usually because it cannot find function role type declarations (see [Using Function Role Type Declarations](using-function-role-type-declarations.md)).

-   Has duplicate callback functions associated with a function role type.

-   Has more callback functions than the maximum supported for a function role type.

-   Has detected that there are wrong or non-existing function names in the Sdv-map.h file after the file has been approved.

Drivers are not required to have every entry point that SDV can analyze. If verification of a particular rule requires a driver entry point that the driver does not have, SDV cancels the verification of that rule and returns a result of **Not Applicable**. This result is not considered to be a failing result.

Unless SDV cannot find any entry points in the driver, it proceeds with its analysis. If the header file used in the analysis is incomplete or incorrect, the verification results are not reliable.

If SDV detects that there are wrong or non-existing function names in the Sdv-map.h file after the file has been approved, SDV exits and issues a warning message like the following example:

```
Warning   &#39;driver&#39; It appears that your sdv-map.h file has an incorrect entry at this line "#define fun_IRP_MJ_PNP DispatchPnpNotExist". Please regenerate your sdv-map.h file.
```

To fix this error, delete the lines in the Sdv.map file that cause the error or regenerate the file.

### <span id="to_regenerate_the_sdv_map_h_file"></span><span id="TO_REGENERATE_THE_SDV_MAP_H_FILE"></span>To regenerate the Sdv-map.h file

1.  Open the Sdv-map.h file and change **//Approved=true** to **//Approved=false**.

2.  Use the **staticdv /scan** command to regenerate the map file, or use a **staticdv /rule** or **staticdv /config** command to run an SDV analysis.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Approving%20the%20Sdv-map.h%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




