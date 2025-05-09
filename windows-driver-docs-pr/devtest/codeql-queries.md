---
title: CodeQL Queries And Suites
description: Reference for the CodeQL queries and suites required to test Windows driver source code for the Windows Hardware Compatibility Program.
keywords:
- dynamic verification tools WDK
- static verification tools WDK
ms.date: 05/09/2025
---

# CodeQL Queries and Suites

As part of the [Microsoft CodeQL GitHub repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools), we provide two query suites to simplify the end-to-end driver developer workflow. The *windows_driver_recommended.qls* query suite is a superset of all the queries Microsoft has deemed valuable for driver developers. The *windows_driver_mustfix.qls* query suite contains queries deemed **"Must-Fix"** for WHCP certification, which must be run and passed in order to pass the Static Tools Logo Test. Both the Must-Fix and Recommended query suites are updated regularly.

### Must-Fix Queries

The subset of queries below are **Must-Fix** for WHCP certification and are also included in the **Recommended Fix** suite.

This set of rules is included in *windows_driver_mustfix.qls*.

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/PointerOverflow.ql*| N/A |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-190/ComparisonWithWiderType.ql*  | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |

The *windows_driver_mustfix.qls* file contains these must fix code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Security queries required to fix when certifying Windows Drivers
- queries: . 
  from: codeql/cpp-queries
  version: 0.9.0
- include:
    query path: 
      - Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql
      - Likely Bugs/Memory Management/PointerOverflow.ql
      - Likely Bugs/Underspecified Functions/TooFewArguments.ql
      - Security/CWE/CWE-190/ComparisonWithWiderType.ql
      - Security/CWE/CWE-253/HResultBooleanConversion.ql
- import: windows-driver-suites/windows_mustfix_partial.qls
  from: microsoft/windows-drivers
```

This set of rules is included in *windows-driver-suites/windows_mustfix_partial.qls*.

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/windows/wdk/deprecated-api](./codeql-windows-driver-wdkdeprecatedapi.md)   | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/WdkDeprecatedApis/wdk-deprecated-api.ql* | N/A |
| [microsoft/Security/CWE/CWE-704/WcharCharConversionLimited](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql)  |*/microsoft/windows-drivers/`<Version>`/microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |

The *windows_mustfix_partial.qls* file contains these must fix code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Security queries required to fix when certifying Windows Drivers
- queries: .
  from: microsoft/windows-drivers
- include:
    query path: 
      - drivers/general/queries/WdkDeprecatedApis/wdk-deprecated-api.ql
      - microsoft/Security/CWE/CWE-704/WcharCharConversionLimited.ql
```

### Recommended Fix Queries

These queries are part of the *windows_driver_recommended.qls* query suite in the [Microsoft GitHub CodeQL repository](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools). The "Common Weakness Enumeration" (CWE) column specifies what kinds of security issues the given query searches for. See [Mitre's page on CWE](https://cwe.mitre.org/) for more details around CWEs.

#### Best Practices

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/offset-use-before-range-check](https://github.com/github/codeql/blob/main/cpp/ql/src/Best%20Practices/Likely%20Errors/OffsetUseBeforeRangeCheck.qhelp)  | *codeql/cpp-queries/`<Version>`/Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql*   | N/A |

#### Likely Bugs

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/bad-addition-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-bad-addition-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html) |
| [cpp/integer-multiplication-cast-to-long](https://codeql.github.com/codeql-query-help/cpp/cpp-integer-multiplication-cast-to-long/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/IntMultToLong.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-192](https://cwe.mitre.org/data/definitions/192.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-681](https://cwe.mitre.org/data/definitions/681.html) |
| [cpp/signed-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-signed-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Arithmetic/SignedOverflowCheck.ql* | N/A |
| [cpp/upcast-array-pointer-arithmetic](https://codeql.github.com/codeql-query-help/cpp/cpp-upcast-array-pointer-arithmetic/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Conversion/CastArrayPointerArithmetic.ql* | [CWE-119](https://cwe.mitre.org/data/definitions/119.html), [CWE-843](https://cwe.mitre.org/data/definitions/843.html) |
| [cpp/pointer-overflow-check](https://codeql.github.com/codeql-query-help/cpp/cpp-pointer-overflow-check/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/PointerOverflow.ql* | N/A |
| [cpp/too-few-arguments](https://codeql.github.com/codeql-query-help/cpp/cpp-too-few-arguments/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Underspecified Functions/TooFewArguments.ql* | N/A |
| [cpp/incorrect-not-operator-usage](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Likely%20Typos/IncorrectNotOperatorUsage.qhelp)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql* | [CWE-480](https://cwe.mitre.org/data/definitions/480.html) |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/SuspiciousSizeof.ql* | [CWE-468](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) |
| [cpp/uninitialized-local](https://github.com/github/codeql/blob/main/cpp/ql/src/Likely%20Bugs/Memory%20Management/UninitializedLocal.qhelp)   | *codeql/cpp-queries/`<Version>`/Likely Bugs/Memory Management/UninitializedLocal.ql* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html), [CWE-665](https://cwe.mitre.org/data/definitions/665.html) |

#### Security

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/conditionally-uninitialized-variable](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-457)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql.* | [CWE-457](https://cwe.mitre.org/data/definitions/457.html) |
| [cpp/unterminated-variadic-call](https://github.com/github/codeql/tree/main/cpp/ql/src/Security/CWE/CWE-121)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-121/UnterminatedVarargsCall.ql* | [CWE-121](https://cwe.mitre.org/data/definitions/121.html) |
| [cpp/suspicious-pointer-scaling](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingChar.qhelp)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/IncorrectPointerScaling.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/suspicious-pointer-scaling-void](https://github.com/github/codeql/blob/main/cpp/ql/src/Security/CWE/CWE-468/IncorrectPointerScalingVoid.qhelp)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql* | [CWE-468](https://cwe.mitre.org/data/definitions/468.html) |
| [cpp/potentially-dangerous-function](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-676/PotentiallyDangerousFunction.ql* | [CWE-676](https://codeql.github.com/codeql-query-help/cpp/cpp-potentially-dangerous-function/)|
| [cpp/incorrect-string-type-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-incorrect-string-type-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-704/WcharCharConversion.ql* | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) |
| [cpp/comparison-with-wider-type](https://codeql.github.com/codeql-query-help/cpp/cpp-comparison-with-wider-type/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-190/ComparisonWithWiderType.ql* | [CWE-190](https://cwe.mitre.org/data/definitions/190.html), [CWE-197](https://cwe.mitre.org/data/definitions/197.html), [CWE-835](https://cwe.mitre.org/data/definitions/835.html) |
| [cpp/hresult-boolean-conversion](https://codeql.github.com/codeql-query-help/cpp/cpp-hresult-boolean-conversion/)   | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-253/HResultBooleanConversion.ql* | [CWE-253](https://cwe.mitre.org/data/definitions/253.html) |
| [cpp/suspicious-add-sizeof](https://codeql.github.com/codeql-query-help/cpp/cpp-suspicious-add-sizeof/) | *codeql/cpp-queries/`<Version>`/Security/CWE/CWE-468/CWE-468/SuspiciousAddWithSizeof.ql*|[CWE-468](https://cwe.mitre.org/data/definitions/468.html)|

The *windows_driver_recommended.qls* file contains these recommended code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Recommended and required queries for Windows Drivers.
- import: windows-driver-suites/windows_mustfix_partial.qls
  from: microsoft/windows-drivers
- import: windows-driver-suites/windows_recommended_partial.qls
  from: microsoft/windows-drivers
- queries: . 
  from: codeql/cpp-queries
  version: 0.9.0
- include:
    query path: 
      - Best Practices/Likely Errors/OffsetUseBeforeRangeCheck.ql
      - Likely Bugs/Arithmetic/IntMultToLong.ql
      - Likely Bugs/Arithmetic/SignedOverflowCheck.ql
      - Likely Bugs/Conversion/CastArrayPointerArithmetic.ql
      - Likely Bugs/Likely Typos/IncorrectNotOperatorUsage.ql
      - Likely Bugs/Memory Management/SuspiciousSizeof.ql
      - Likely Bugs/Memory Management/UninitializedLocal.ql
      - Security/CWE/CWE-121/UnterminatedVarargsCall.ql
      - Security/CWE/CWE-457/ConditionallyUninitializedVariable.ql
      - Security/CWE/CWE-468/IncorrectPointerScaling.ql
      - Security/CWE/CWE-468/IncorrectPointerScalingVoid.ql
      - Security/CWE/CWE-468/SuspiciousAddWithSizeof.ql
      - Security/CWE/CWE-676/PotentiallyDangerousFunction.ql
      - Security/CWE/CWE-704/WcharCharConversion.ql
      - Likely Bugs/Arithmetic/BadAdditionOverflowCheck.ql
      - Likely Bugs/Memory Management/PointerOverflow.ql
      - Likely Bugs/Underspecified Functions/TooFewArguments.ql
      - Security/CWE/CWE-190/ComparisonWithWiderType.ql
      - Security/CWE/CWE-253/HResultBooleanConversion.ql
```

These queries are part of *windows_recommended_partial.qls*.

#### Likely Bugs - windows_recommended_partial.qls

| ID                       | Location   | [Common Weakness Enumeration](https://cwe.mitre.org/)   |
| ------------------------ | ---------- | ------------------------------------------------------- |
| [cpp/paddingbyteinformationdisclosure](./codeql-windows-driver-padding-byte-information-disclosure.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql* | N/A |
| [cpp/badoverflowguard](./codeql-windows-driver-badoverflowguard.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Conversion/BadOverflowGuard.ql* | N/A |
| [cpp/infiniteloop](./codeql-windows-driver-infiniteloop.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Conversion/InfiniteLoop.ql* | N/A |
| [cpp/uninitializedptrfield](./codeql-windows-driver-uninitializedptrfield.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/UninitializedPtrField.ql* | N/A |
| [cpp/use-after-free](./codeql-windows-driver-useafterfree.md)   | *microsoft/windows-drivers/`<Version>`/microsoft/Likely Bugs/Memory Management/UseAfterFree/UseAfterFree.ql* | N/A |

#### Security - windows_recommended_partial.qls

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/weak-crypto/cng/hardcoded-iv](./codeql-windows-driver-hardcodedivcng.md)   | */microsoft/windows-drivers/`<Version>`/microsoft/Security/Crytpography/HardcodedIVCNG.ql* | N/A |

#### Drivers - General

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/drivers/ke-set-event-pageable](./codeql-windows-driver-keseteventpageable.md) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/KeSetEventPageable/KeSetEventPageable.ql*  | No associated CA check  |
| [cpp/drivers/role-type-correctly-used](./codeql-windows-driver-roletypecorrectlyused.md) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/RoleTypeCorrectlyUsed/RoleTypeCorrectlyUsed.ql* | No associated CA check|
| [cpp/drivers/extended-deprecated-apis](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/ExtendedDeprecatedApis/ExtendedDeprecatedApis.ql) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/ExtendedDeprecatedApis.ql* | [C28719 Warning](28719-banned-api-usage-use-updated-function-replacement.md), [C28726 Warning](28726-banned-api-usage-use-updated-function-replacement.md), [C28735 Warning](28735-banned-crimson-api-usage.md), [C28750 Warning](28750-banned-istrlen-usage.md) |
| [cpp/drivers/irql-not-saved](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlNotSaved/) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlNotSaved/IrqlNotSaved.ql* | [C28158 Warning](28158-no-irql-was-saved.md) |
| [cpp/drivers/irql-not-used](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlNotUsed/) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlNotUsed/IrqlNotUsed.ql* | [C28157 Warning](28157-function-irql-never-restored.md) |
| [cpp/drivers/irql-set-too-high](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlSetTooHigh) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlTooHigh/IrqlTooHigh.ql* | [C28150 Warning](28150-function-causes-irq-level-to-be-set-above-max.md) |
| [cpp/drivers/irql-too-low](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries//IrqlTooLow) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlTooLow/IrqlTooLow.ql* | [C28120 Warning](28120-irql-execution-too-low.md) |
| [cpp/drivers/irql-set-too-high](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlTooHigh) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlSetTooHigh/IrqlTooHigh.ql* | [C28121 Warning](28121-irq-execution-too-high.md) |
| [cpp/drivers/irql-set-too-low](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/IrqlSetTooLow) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/IrqlSetTooLow/IrqlSetTooLow.ql* | [C28124 Warning](28124-call-below-minimum-irq-level.md) |
| [cpp/drivers/pool-tag-integral](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/PoolTagIntegral) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/PoolTagIntegral/PoolTagIntegral.ql* | [C28134 Warning](28134-pool-tag-type-should-be-integral.md) |
| [cpp/drivers/str-safe](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/general/queries/StrSafe) | */microsoft/windows-drivers/`<Version>`/drivers/general/queries/StrSafe/StrSafe.ql* | [C28146 Warning](28146-kernel-mode-drivers-should-use-ntstrsafe.md) |

#### Drivers - WDM

| ID                       | Location   | [Code Analysis Warning](prefast-for-drivers-warnings.md)   |
| ------------------------ | ---------- | ---------------------------------------------------------- |
| [cpp/drivers/illegal-field-access](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/IllegalFieldAccess)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldAccess/IllegalFieldAccess.ql* | [C28128 Warning](28128-structure-member-directly-accessed.md) |
| [cpp/drivers/illegal-field-access2](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries//IllegalFieldAccess2) | */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldAccess2/IllegalFieldAccess2.ql* | [C28175 Warning](28175struct-member-should-not-be-accessed-by-driver.md) |
| [cpp/drivers/illegal-field-write](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/IllegalFieldWrite) | */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/IllegalFieldWrite/IllegalFieldWrite.ql* | [C28176 Warning](28176-struct-member-should-not-be-modified-by-driver.md) |
| [cpp/drivers/opaque-mdl-use](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/OpaqueMdlUse)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlUse.ql* | (No associated CA check) |
| [cpp/drivers/opaque-mdl-write](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/OpaqueMdlWrite)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlWrite.ql* | [C28145 Warning](28145-opaque-mdl-structure-should-not-be-modified.md) |
| [cpp/drivers/pending-status-error](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/PendingStatusError)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/PendingStatusError/PendingStatusError.ql* | [C28143 Warning](28143-iomarkirppending-must-return-statuspending.md) |
| [cpp/drivers/wrong-dispatch-table-assignment](https://github.com/microsoft/Windows-Driver-Developer-Supplemental-Tools/blob/main/src/drivers/wdm/queries/WrongDispatchTableAssignment)| */microsoft/windows-drivers/`<Version>`/drivers/wdm/queries/WrongDispatchTableAssignment/WrongDispatchTableAssignment.ql* | [C28169 Warning](28169-dispatch-function-does-not-have-proper-annotation.md) |

The *windows-driver-suites/windows_recommended_partial.qls* file contains these recommended code queries.

```text
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

- description: Recommended and required queries for Windows Drivers.
- import: windows-driver-suites/windows_mustfix_partial.qls
- queries: .
  from: microsoft/windows-drivers
- include:
    query path: 
      - microsoft/Likely Bugs/Boundary Violations/PaddingByteInformationDisclosure.ql
      - microsoft/Likely Bugs/Conversion/BadOverflowGuard.ql
      - microsoft/Likely Bugs/Conversion/InfiniteLoop.ql
      - microsoft/Likely Bugs/Memory Management/UseAfterFree/UseAfterFree.ql
      - microsoft/Likely Bugs/UninitializedPtrField.ql
      - microsoft/Security/Crytpography/HardcodedIVCNG.ql
      - drivers/general/queries/KeSetEventPageable/KeSetEventPageable.ql
      - drivers/general/queries/RoleTypeCorrectlyUsed/RoleTypeCorrectlyUsed.ql
      - drivers/general/queries/DefaultPoolTag/DefaultPoolTag.ql
      - drivers/general/queries/ExaminedValue/ExaminedValue.ql
      - drivers/general/queries/ExtendedDeprecatedApis/ExtendedDeprecatedApis.ql
      - drivers/general/queries/IrqlNotSaved/IrqlNotSaved.ql
      - drivers/general/queries/IrqlNotUsed/IrqlNotUsed.ql
      - drivers/general/queries/IrqlTooHigh/IrqlTooHigh.ql
      - drivers/general/queries/IrqlTooLow/IrqlTooLow.ql
      - drivers/general/queries/IrqlSetTooHigh/IrqlTooHigh.ql
      - drivers/general/queries/IrqlSetTooLow/IrqlSetTooLow.ql
      - drivers/general/queries/PoolTagIntegral/PoolTagIntegral.ql
      - drivers/general/queries/StrSafe/StrSafe.ql
      - drivers/wdm/queries/IllegalFieldAccess/IllegalFieldAccess.ql
      - drivers/wdm/queries/IllegalFieldAccess2/IllegalFieldAccess2.ql
      - drivers/wdm/queries/IllegalFieldWrite/IllegalFieldWrite.ql
      - drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlUse.ql
      - drivers/wdm/queries/OpaqueMdlUse/OpaqueMdlWrite.ql
      - drivers/wdm/queries/PendingStatusError/PendingStatusError.ql
      - drivers/wdm/queries/WrongDispatchTableAssignment/WrongDispatchTableAssignment.ql
```
## Related Content

- [Run the CodeQL analysis on your driver code](/devtest/static-tools-and-codeql.md)
- [CodeQL Overview](/devtest/codeql-overview.md)
- [CodeQL FAQ](/devtest/codeql-faq.md)