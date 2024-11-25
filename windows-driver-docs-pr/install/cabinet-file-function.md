---
title: Cabinet File Functions
description: CAB files are used to organize the installation files that are copied to the user's system.
keywords:
- SetupAPI functions WDK , cabinet files
- .cab files
- CAB files
ms.date: 11/25/2024
---

# Cabinet file functions

A cabinet (CAB) file is a single file, usually with a .*cab* extension, that contains several compressed files as a file library. CAB files are used to organize the installation files that are copied to the user's system. A compressed file can be spread over several CAB files.

The following functions iterate through all the files in a cabinet and send notifications to a callback function for each file found.

- [**SetupIterateCabinetA**](/windows/win32/api/setupapi/nf-setupapi-setupiteratecabineta)
- [**SetupIterateCabinetW**](/windows/win32/api/setupapi/nf-setupapi-setupiteratecabineta)

## See also

- [Cabinet Files](/windows/win32/msi/cabinet-files)
