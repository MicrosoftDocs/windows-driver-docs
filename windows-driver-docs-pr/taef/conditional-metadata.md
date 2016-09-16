---
title: Conditional Metadata
description: Conditional Metadata
ms.assetid: A1C223AB-E9BB-480e-B9ED-75989FD34479
---

# Conditional Metadata


Sometimes it is useful to have metadata values change depending on runtime values. Conditional metadata allows module, class, or method metadata to only be applied in certain conditions based on [runtime parameters](runtime-parameters.md).

## <span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>Syntax


To make metadata conditional, add a condition surrounded by square brackets after the metadata name. The condition must be in the format of our [selection query language](selection.md). The values for the variables come from [runtime parameters](runtime-parameters.md).

For example, suppose a test has the following metadata:

```
TEST_METHOD_PROPERTY(L"RunAs", L"Elevated")
TEST_METHOD_PROPERTY(L"Ignore[@NoElevation=true]", L"true")
```

Then when TAEF loads the DLL, it will evaluate the "@NoElevation=true" condition based on the runtime parameters. So if the user sets the "NoElevation" runtime parameter to true, then the test will have metadata applied to it with the name "Ignore" and the value "true".

If multiple conditional metadata appear in one test, each is evaluated independently in the same manner. This can be useful if you want a test to recognize multiple possible values of a runtime parameter.

```
TEST_METHOD_PROPERTY(L"Data:MyTestData[@TestCaseLevel=&#39;Low&#39;]", L"{ Datum1, Datum2, Datum3 }")
TEST_METHOD_PROPERTY(L"DataSource[@TestCaseLevel=&#39;High&#39;]", L"Pict:FullDataSet.model?Order=3")
```

If a test has the metadata shown above and the user sets TestCaseLevel to Low, the test will only be invoked three times due to the [lightweight data source](light-weight-data-driven-testing.md). If the user sets TestCaseLevel to High, the [PICT data source](pict-data-source.md) will be used to generate many more parameters for the test. If TestCaseLevel is not set to High or Low, then no metadata will be added.

## <span id="default"></span><span id="DEFAULT"></span>Default Values


When you want to add a metadata only when no other conditions for that particular metadata name have evaluated to true, you can append the metadata name with *\[default\]*.

```
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;Low&#39;]", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order[default]", L"2")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;High&#39;]", L"3")
```

If a test has the above metadata and the user does not set TestCaseLevel to Low or High, Pict:Order will be set to 2. If the user sets TestCaseLevel to Low or High, Pict:Order will be set to 1 or 3, respectively. The value of 2 will not apply because at least one condition on that test for Pict:Order evaluated to true.

Be careful not to leave off the \[default\] if it is needed.

```
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;Low&#39;]", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order", L"2") // This should have [default]
TEST_METHOD_PROPERTY(L"Pict:Order[@TestCaseLevel=&#39;High&#39;]", L"3")
```

If TestCaseLevel is set to Low, the above set of metadata is equivalent to the following set of metadata:

```
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyTest.model")
TEST_METHOD_PROPERTY(L"Pict:Order", L"1")
TEST_METHOD_PROPERTY(L"Pict:Order", L"2")
```

In this case, it is unspecified whether the PICT data source will use the "1" or the "2" for the PICT order.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Conditional%20Metadata%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




