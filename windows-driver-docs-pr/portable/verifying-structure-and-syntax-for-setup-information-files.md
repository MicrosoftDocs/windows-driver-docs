---
Description: Verifying Structure and Syntax for Setup Information Files
title: Verifying Structure and Syntax for Setup Information Files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Verifying Structure and Syntax for Setup Information Files


The Windows Driver Kit (WDK) supplies a set of Perl scripts that are referred to as the ChkINF tool. These scripts verify the structure and syntax of setup information (.inf) files. For more information about these scripts, see the Driver Development Tools section of the WDK documentation.

All WPD .inf files must invoke the UMDF co-installer. This means that whenever a CoInstallers section is declared, a \[CopyFiles\] directive must exist. If your driver does not require any additional co-installer binaries (and therefore does not need a CopyFiles directive), you can satisfy the requirement by declaring an empty CopyFiles section and referencing it from within the CoInstallers section.

 

 




