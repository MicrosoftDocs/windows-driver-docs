---
title: Conditional Metadata
description: Conditional Metadata
ms.assetid: A1C223AB-E9BB-480e-B9ED-75989FD34479
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Conditional Metadata


Sometimes it is useful to have metadata values change depending on runtime values. Conditional metadata allows module, class, or method metadata to only be applied in certain conditions based on [runtime parameters](runtime-parameters.md).

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


To make metadata conditional, add a condition surrounded by square brackets after the metadata name. The condition must be in the format of our [selection query language](selection.md). The values for the variables come from [runtime parameters](runtime-parameters.md).

For example, suppose a test has the following metadata:

```cpp
TEST_METHOD_PROPERTY(L"RunAs", L"Elevated")
TEST_METHOD_PROPERTY(L"Ignore[@NoElevation=true]", L"true")
```

Then when TAEF loads the DLL, it will evaluate the "@NoElevation=true" condition based on the runtime parameters. So if the user sets the "NoElevation" runtime parameter to true, then the test will have metadata applied to it with the name "Ignore" and the value "true".

If multiple conditional metadata appear in one test, each is evaluated independently in the same manner. This can be useful if you want a test to recognize multiple possible values of a runtime parameter.

```cpp
TEST_METHOD_PROPERTY(L"Data:MyTestData[@TestCaseLevel=&#39;Low&#39;]", L"{ Datum1, Datum2, Datum3 }")
TEST_METHOD_PROPERTY(L"DataSource[@TestCaseLevel=&#39;High&#39;]", L"Pict:FullDataSet.model?Order=3")
```

If a test has the metadata shown above and the user sets TestCaseLevel to Low, the test will only be invoked three times due to the [lightweight data source](light-weight-data-driven-testing.md). If the user sets TestCaseLevel to High, the [PICT data source](pict-data-source.md) will be used to generate many more parameters for the test. If TestCaseLevel is not set to High or Low, then no metadata will be added.

## <span id="default"></span><span id="DEFAULT"></span>Default Values


When you want to add a metadata only when no other conditions for that particular metadata name have evaluated to true, you can append the metadata name with *\[default\]*.

```cpp
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;Low&#39;]", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order[default]", L"2")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;High&#39;]", L"3")
```

If a test has the above metadata and the user does not set TestCaseLevel to Low or High, Pict:Order will be set to 2. If the user sets TestCaseLevel to Low or High, Pict:Order will be set to 1 or 3, respectively. The value of 2 will not apply because at least one condition on that test for Pict:Order evaluated to true.

Be careful not to leave off the \[default\] if it is needed.

```cpp
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;Low&#39;]", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order", L"2") // This should have [default]
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;High&#39;]", L"3")
```

If TestCaseLevel is set to Low, the above set of metadata is equivalent to the following set of metadata:

```cpp
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order", L"2")
```

In this case, it is unspecified whether the PICT data source will use the "1" or the "2" for the PICT order.

 

 





