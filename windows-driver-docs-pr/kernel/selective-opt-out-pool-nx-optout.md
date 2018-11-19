---
title: Selective Opt-Out POOL_NX_OPTOUT
description: You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL_NX_OPTOUT.
ms.assetid: 15AA7CFA-5BEC-4E45-B222-0DE2D620E099
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Selective Opt-Out: POOL\_NX\_OPTOUT


You can globally enable one of the no-execute (NX) pool opt-in mechanisms for a set of driver source files, and then override this opt-in mechanism for one or more selected source files with POOL\_NX\_OPTOUT. This allows the selected source files to continue to use executable nonpaged memory. You can use the POOL\_NX\_OPTOUT opt-out mechanism with either the POOL\_NX\_OPTIN or the POOL\_NX\_OPTIN\_AUTO opt-in mechanism. For more information, see [NX Pool Opt-In Mechanisms](nx-pool-opt-in-mechanisms.md).

To use the POOL\_NX\_OUTPUT opt-out mechanism to override the opt-in mechanism in a selected source file, add the following definition to this file:

`#define POOL_NX_OPTOUT 1`

This definition overrides the global opt-in settings in the selected file, and prevents instances of the **NonPagedPool** constant name from being replaced. Insert this definition into the file before the first instance of **NonPagedPool** in the file.

An alternative to using the POOL\_NX\_OPTOUT opt-out mechanism in a source file is to explicitly replace each instance of **NonPagedPool** in the file with **NonPagedPoolExecute**.

 

 




