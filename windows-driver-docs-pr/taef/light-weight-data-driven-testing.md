---
title: Light-weight Data-driven Testing
description: Light-weight Data-driven Testing
ms.assetid: A7070E38-A545-4156-B441-C0E6ACE569F5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="taef.light-weight_data-driven_testing"></span>Light-weight Data-driven Testing


There are likely to be scenarios where a complete XML DataSource and Table based data-driven testing may be too heavy for your test scenario needs. Light-weight data-driven testing allows a quick and easy way to get data-driven testing support when the data for your test is simple and can easily be expressed as a metadata. Let's use an example and see how.

The data for the light weight data-driven test is expressed as a set of metadata (at the test, class or module level). For each of the values in this set, the test methods in concern, along with the associated setup and teardown methods will be executed for each value in the set. Let's take a look at how to author this in native code:

```cpp
1  #include "WexString.h"
2  #include "WexTestClass.h"
3
4  using namespace WEX::Common;
5  using namespace WEX::TestExecution;
6  using namespace WEX::Logging;

7  namespace WEX { namespace TestExecution { namespace Examples
8  {
9      class SimpleDataDrivenExample
10     {
11         TEST_CLASS(SimpleDataDrivenExample);
12         ...
13         BEGIN_TEST_METHOD(SetsOfDataTest)
14             TEST_METHOD_PROPERTY(L"Data:Color", L"{Purple, Maroon, Brown}")
15         END_TEST_METHOD()
16     };
```

Notice the parameter values for TEST\_METHOD\_PROPERTY in line 14. The test metadata value starts with a "{" and ends with a "}" indicating that a comma or semicolon separated list of values have been specified. TAEF will re-execute the test method in concern, SetsOfDataTest() once for each value in this set.

Also notice that the metadata name starts with a "Data:". This implies that the metadata set is really specifying variations for the data-driven test parameters and would be available to the actual test method much like data parameters from a Table based data-driven test like so:

```cpp
11     ...
12
13     void SimpleDataDrivenExample::SetsOfDataTest()
14     {
15         String color;
16         if (SUCCEEDED(TestData::TryGetValue(L"color", color)))
17         {
18             Log::Comment(L"Color retrieved was " + color);
19         }
20     }
21 } /* namespace Examples */ } /* namespace TestExecution */ } /* namespace WEX */
```

While working with managed code, the specification and retrieval of data set is much like the native example. Let's take a look:

```cpp
1  namespace WEX.Examples
2  {
3      using Microsoft.VisualStudio.TestTools.UnitTesting;
4      using System;
5      using System.Collections;
6      using System.Data;
7      using WEX.Logging.Interop;
8      using WEX.TestExecution;
9
10     [TestClass]
11     public class CSharpDataDrivenSimpleExample
12     {
13         ...
14         [TestMethod]
15         [TestProperty("Data:Color", "{Red, Green, Blue}")]
16         public void SetsOfMetadataTest()
17         {
18             Log.Comment("Color is " + m_testContext.DataRow["Color"]);
19         }
20
21         public TestContext TestContext
22         {
23             get { return m_testContext; }
24             set { m_testContext = value; }
25         }
26
27         private TestContext m_testContext;
28     }
29 }
```

Just like in the case of table based data-driven tests, sets of data specified as metadata, will allow retrieval via TestContext.DataRow.**Note that to keep the data-driven test light weight, the parameter type will always be WEX::Common::String (in native code) and String(in managed code)**

**If multiple of data values are specified, a catersian product of all possible values will be obtained and the test method will be invoked for each combination.**

It is further possible to have some metadata sets (like [ThreadingModel metadata sets](threading-models.md)) as well as data sets specified for the same test method. In such a case a combinatorial expansion of all metadata sets and data sets will be produced by TAEF and the test methods in concern will be invoked with every combination.

## <span id="metadataExpansion"></span><span id="metadataexpansion"></span><span id="METADATAEXPANSION"></span>Special cases - data-driven test with a sets of metadata or data


You could have a test method dependent on Table based data-driven test as well as specify a sets of data or metadata for it. For example, a test method could have parameters "size" and "color" specified in the table based data-driven test and want all the rows to be executed once with "transparency" parameter set to true and then set to false. In such a case, "transparency" could be specified as a set "{true, false}" for the data-driven test. **It is important to note that in case of conflicts of parameter in a metadata set verses table based data-driven Row, the Row level parameter type and value will override the metadata set value.**

## <span id="Executing_tests_with_Sets_of_data___metadata"></span><span id="executing_tests_with_sets_of_data___metadata"></span><span id="EXECUTING_TESTS_WITH_SETS_OF_DATA___METADATA"></span>Executing tests with Sets of data / metadata


Execution of tests containing sets of data is quite intuitive. Let's take a look at the /listproperties output for our example tests:

``` syntax
1   te Examples\CPP.DataDriven.Example.dll /name:*SetsOfDataTest* /listproperties
2
3   Test Authoring and Execution Framework v2.9.3k for x64
4
5           f:\ Examples\CPP.SimpleDataDriven.Example.dll
6               WEX::TestExecution::Examples::SimpleDataDrivenExample<
7                   WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet0
8                           Property[Data:Color] = {Purple, Maroon, Brown}
9
10                          Data[Color] = Purple
11
12                  WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet1
13                          Property[Data:Color] = {Purple, Maroon, Brown}
14
15                          Data[Color] = Maroon
16
17                  WEX::TestExecution::Examples::SimpleDataDrivenExample::SetsOfDataTest#metadataSet2
18                          Property[Data:Color] = {Purple, Maroon, Brown}
19
20                          Data[Color] = Brown
```

Notice lines 7, 12, and 17 in the example above. A metadata set index gets appended to each invocation of the test method with the value in the data set. This index is of the form:

```cpp
<namespace qualified test method name>#metadataSet<metadataIndex>
```

Lines 8, 13, and 18 show the metadata set that has been specified for this light-weight data-driven testing support. In this case the set consists of colors purple, maroon and brown. Lines 10, 15, and 20 show the actual value from this set which is active for the current invocation of the test. In the case of SetsOfMetadataTest\#metadataSet1, the second invocation of this method, the active parameter value from the set is "Maroon"

You can select on the Data value or name just like you could in Table based data-driven tests. For example you can select SetsOfDataTest\#metadataSet1 by a selection query like **/select:@Data:Color='Maroon'** or **/name:\*\#metadataSet1**

For quick reference, /listproperties output from the manged test example is shown below:

``` syntax
te Examples\CSharp.DataDriven.Example.dll /name:*SetsOfMetadataTest* /listproperties

Test Authoring and Execution Framework v2.9.3k for x64

        f:\ Examples\CSharp.DataDrivenSimple.Example.dll
            WEX.Examples.CSharpDataDrivenSimpleExample
                WEX.Examples.CSharpDataDrivenSimpleExample.NonDataDrivenTest
                WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet0
                        Property[Data:Color] = {Red, Green, Blue}

                        Data[Color] = Red

                WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet1
                        Property[Data:Color] = {Red, Green, Blue}

                        Data[Color] = Green

                WEX.Examples.CSharpDataDrivenSimpleExample.SetsOfMetadataTest#metadataSet2
                        Property[Data:Color] = {Red, Green, Blue}

                        Data[Color] = Blue
```

 

 





