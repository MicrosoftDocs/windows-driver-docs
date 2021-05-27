---
title: What the Checked Build Checks
description: What the Checked Build Checks
keywords:
- checked builds WDK , checks performed
- parameter validation checks WDK
- internal checks WDK
- correctness checks WDK
- consistency checks WDK
- informational checks WDK
- tracing output checks WDK
ms.date: 05/08/2020
ms.localizationpriority: medium
---

# What the Checked Build Checks

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

The checked build includes a significant number of debugging checks that are normally not present in the system. These checks include:

- **Parameter validation checks**

    These checks ensure that the Windows operating system code ordinarily runs with as little overhead as possible. As a result, the NT-based operating systems implement the policy that all components running in kernel-mode, including drivers, implicitly "trust" each other. Thus, parameters that are passed from one kernel-mode component to another (such as parameters passed on function calls) are typically subject to minimal validation. The checked build of the operating system enables many additional parameter validation checks.

- **Internal checks for operating system correctness and consistency**

    These checks typically verify the correctness of key algorithms and data structures in the operating system. Checks of this type can also be inserted by one of the Windows developers during the operating system debugging process to help isolate difficult problems.

- **Informational checks and tracing output**

    These checks, and the resulting output that is displayed in the debugger, are designed to assist debugging of drivers or other system-level components. Often, these types of checks must be individually enabled by setting debug flags--typically using the debugger--internally in the component of interest. The existence of such checks and their debug output may vary from release to release of the operating system. When such checks exist, they are often documented in Microsoft Knowledge Base articles.

Most of the checks that appear in the checked build determine if the values in parameters or data structures are within anticipated typical ranges. During operation of the system, it might be possible, under certain rare circumstances, for a particular parameter or value to fall outside the typically anticipated range.

Thus, even when one of the checks in the checked build fails, it does not necessarily mean that a catastrophic failure has occurred. In fact, a failing check in the checked build does not necessarily mean that something has gone wrong. It merely means that a particular check has failed. You must be able to *explain* the reason for the failure.

Do not ignore problems that are identified by the checked build. The key to successfully debug drivers with the checked build is to be sure that you can explain the reason for each failure that the checked build finds.
