---
title: Approving the Sdv-map.h File
description: Approving the Sdv-map.h File
ms.assetid: eb192eb2-7a2c-47eb-846e-3d641d5046a8
keywords:
- Sdv-map.h WDK Static Driver Verifier , approving
- approving Sdv-map.h
ms.date: 04/20/2017
ms.localizationpriority: medium
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
Warning 'driver' It appears that your sdv-map.h file has an incorrect entry at this line "#define fun_IRP_MJ_PNP DispatchPnpNotExist". Please regenerate your sdv-map.h file.
```

To fix this error, delete the lines in the Sdv.map file that cause the error or regenerate the file.

### <span id="to_regenerate_the_sdv_map_h_file"></span><span id="TO_REGENERATE_THE_SDV_MAP_H_FILE"></span>To regenerate the Sdv-map.h file

1.  Open the Sdv-map.h file and change **//Approved=true** to **//Approved=false**.

2.  Use the **staticdv /scan** command to regenerate the map file, or use a **staticdv /rule** or **staticdv /config** command to run an SDV analysis.

 

 





