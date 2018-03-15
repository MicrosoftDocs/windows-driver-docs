---
title: Run a "staticdv /clean" command in drivername
description: Run a "staticdv /clean" command in drivername
ms.assetid: 179ade54-625f-427e-b680-f9814c41808f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Run a "staticdv /clean" command in :&lt;drivername&gt;


SDV reports this error when you submit a command to verify a driver before deleting the files from a previous verification.

When SDV verifies a driver, it creates files in which it records the results of the verification. It uses these files to create the display in the Static Driver Verifier Report. If these previous versions of these files already exist in the directory, SDV does not overwrite the files. Instead, it displays this message asking you to delete the files intentionally.

To eliminate the error, use the **/clean** command option, or click **Clean** in Static Driver Verifier. This deletes the files from the previous verification.

If the approved flag is set to true in the Sdv-map.h file (Approved=true), SDV retains the Sdv-map.h file so that you do not have to scan the driver entry routine again or approve the file contents.

For more information about **/clean** and other commands, see [Static Driver Verifier commands (MSBuild)](-static-driver-verifier-commands--msbuild-.md).

 

 





