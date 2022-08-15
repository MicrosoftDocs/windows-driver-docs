---
title: C28650 warning
description: The type for which 0 is being used does not treat it as failure case.
ms.date: 04/20/2017
f1_keywords: 
  - "C28650"
---

# C28650


warning C28650: The type for which !0 is being used does not treat it as failure case.

Returning a status value such as !TRUE is not the same as returning a status value that indicates failure.

Certain data types such as **NTSTATUS** and **HRESULT** have associated macros that classify values of these types into SUCCESS or FAILURE. These macros check the most significant bit of the returned value or values to determine this. Thus, 0 and 1 are both classified as SUCCESS values.

The proper way to fix this warning is to return a proper error code instead of a generic value such as -1.

 

 





