---
title: Data-driven Class
description: Data-driven Class
ms.assetid: 2998D5BB-A873-4df9-86B2-88937736862F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="taef.data-driven_class"></span>Data-driven Class


Please make sure that you are familiar with the basic execution of TAEF and know how to author tests using it before proceeding with this section. You might also want to go through the simple data-driven test example walk-through. In this section, you will make a data-driven test class that is based upon a *table based* data-driven test, but the same approach applies to *WMI based* or *PICT based* data-driven tests.

## <span id="whentouse_ddc"></span><span id="WHENTOUSE_DDC"></span>When to use a Data-driven Class?


There are times when multiple tests could depend upon the same input data. When testing APIs, you may want to run multiple API tests with the same data in order to get a consistent view of the API behaviour. When performing scenario level tests, you may want to ensure that all of the steps in your scenario are tested with the same data. At these times, it is useful to specify the test data at the class level.

## <span id="authoring_ddc"></span><span id="AUTHORING_DDC"></span>Authoring Data-driven Class


You specify that a given class is data-driven in a similar way to how you specify that a given test is data-driven. You apply the **DataSource** metadata at the class-level. The value identifies the particular data source of interest. The following example shows how to specify these properties for data-driven classes:

### <span id="native1_authoring"></span><span id="NATIVE1_AUTHORING"></span>Native code

```cpp
1     class 2     {
2         BEGIN_TEST_CLASS(DataDrivenClassExample)
3             TEST_CLASS_PROPERTY(L"DataSource", L"Table:DataDrivenClassExample.xml#ClassTable")
4         END_TEST_CLASS()
5
6         TEST_METHOD(Test1);
7       {
8         int size;
9           if (SUCCEEDED(<span class="style2">TestData::TryGetValue(L"size", size)</span>))
10          {
11              VERIFY_ARE_NOT_EQUAL(size, 0);
12              Log::Comment(String().Format(L"Size retrieved was %d", size));
13          }
14  
15          String color;
16          if (SUCCEEDED(<span class="style2">TestData::TryGetValue(L"color", color)</span>))
17          {
18              Log::Comment(L"Color retrieved was " + color);
19          }
20      }
21         TEST_METHOD(Test2);
22      {
23          int size;
24          if (SUCCEEDED(<span class="style2">TestData::TryGetValue(L"size", size)</span>))
25          {
26              VERIFY_ARE_NOT_EQUAL(size, 0);
27              Log::Comment(String().Format(L"Size retrieved was %d", size));
28          }
29  
30          String color;
31          if (SUCCEEDED(<span class="style2">TestData::TryGetValue(L"color", color)</span>))
32          {
33              Log::Comment(L"Color retrieved was " + color);
34          }
35      } 
36    };
```

### <span id="managed1_authoring"></span><span id="MANAGED1_AUTHORING"></span>Managed code

```cpp
1     [TestClass]
2     public class CSharpDataDrivenClassExample
3     {
4         [ClassInitialize]
5         [DataSource("Table:CSharpDataDrivenClassExample.xml#ClassTable")]
6         public static void MyClassInitialize(Object testContext)
7         {
8         }
9
10        [TestMethod]
11        public void Test1()
12        {
13            int size = (int)m_testContext.DataRow["Size"];
14            Verify.AreNotEqual(size, 0);
15            Log.Comment("Size is " + size.ToString());
16
18            Log.Comment("Color is " + m_testContext.DataRow["Color"]);
19        }
20
21        [TestMethod]
22        public void Test2()
23        {
24            int size = (int)m_testContext.DataRow["Size"];
25            Verify.AreNotEqual(size, 0);
26            Log.Comment("Size is " + size.ToString());
27
28            Log.Comment("Color is " + m_testContext.DataRow["Color"]);
29        }
30
31        public TestContext TestContext
32        {
33            get { return m_testContext; }
34            set { m_testContext = value; }
35        }
36
37        private TestContext m_testContext;
38    }
```

In these examples, line 3 in the **Native code** example and line 5 in the **Managed code** example are the recommended ways to specify the datasource for a data-driven test class in TAEF.

In the **Managed code** example above, lines 13, 18, 24, and 28 show how data is made available to the test methods for managed code.

In the following code example, lines 4, 11, 20, and 27 show how data is made available to the test methods for native code. Notice that ***you make the data that you defined in the data-driven class's table (rows) available to the test methods in the class (Test1 and Test2) in exactly the same way that you would for a data-driven test.***

### <span id="native2_authoring"></span><span id="NATIVE2_AUTHORING"></span>

You construct the **DataSource** XML file for a data-driven class in exactly the same way as you would for a data-driven test. The following examples show the XML files for native and managed classes.

### <span id="native3_authoring"></span><span id="NATIVE3_AUTHORING"></span>Native

```cpp
1 <?xml version="1.0"?>
2 <Data>
3   <Table Id="ClassTable">
4     <ParameterTypes>
5       <ParameterType Name="Size">int</ParameterType>
6     </ParameterTypes>
7     <Row>
8       <Parameter Name="Size">4</Parameter>
9       <Parameter Name="Color">White</Parameter>
10    </Row>
11    <Row>
12      <Parameter Name="Size">10</Parameter>
13      <Parameter Name="Color">Black</Parameter>
14    </Row>
15    <Row>
16      <Parameter Name="Size">9</Parameter>
17      <Parameter Name="Color">Orange</Parameter>
18    </Row>
19    <Row>
20      <Parameter Name="Size">9</Parameter>
21      <Parameter Name="Color">Blue</Parameter>
22    </Row>
23  </Table>
24</Data>
```

### <span id="manged2_authoring"></span><span id="MANGED2_AUTHORING"></span>Managed

```cpp
1 <?xml version="1.0"?>
2 <Data>
3   <Table Id="ClassTable">
4     <ParameterTypes>
5       <ParameterType Name="Size">Int32</ParameterType>
6       <ParameterType Name="Color">String</ParameterType>
7     </ParameterTypes>
8     <Row>
9      <Parameter Name="Size">4</Parameter>
10      <Parameter Name="Color">White</Parameter>
11    </Row>
12    <Row>
13      <Parameter Name="Size">10</Parameter>
14      <Parameter Name="Color">Black</Parameter>
15    </Row>
16    <Row>
17      <Parameter Name="Size">9</Parameter>
18      <Parameter Name="Color">Orange</Parameter>
19    </Row>
20    <Row>
21      <Parameter Name="Size">9</Parameter>
22      <Parameter Name="Color">Blue</Parameter>
23    </Row>
24  </Table>
25</Data>
```

## <span id="behindscene_ddc"></span><span id="BEHINDSCENE_DDC"></span>Behind the Scenes OR What to Expect?


By default, when you author tests in TAEF, the execution order within a class is the same as the order in which you coded the test methods in the class. Therefore, in the previous examples, **Test1** will always execute before **Test2**. Because the class that contains **Test1** and **Test2** is a data-driven class, all of the class methods will execute once for each data ROW that you defined in **DataSource**. In other words, **Test1** and **Test2** execute for Row \#0. Then, these methods execute in the same order for Row \#1 and so on until TAEF executes all rows.

## <span id="executing_ddc"></span><span id="EXECUTING_DDC"></span>Executing tests in a Data-driven Class


If you execute the example test binaries with the **/list** command option, the execution order from the previous section becomes clear.

### <span id="native1_executing"></span><span id="NATIVE1_EXECUTING"></span>Native

``` syntax
TE.exe Examples\CPP.AdvancedDataDriven.Examples.dll /name:*class* /list
Test Authoring and Execution Framework v2.9.3k for x86

        F:\ Examples\CPP.AdvancedDataDriven.Examples.dll
            WEX::TestExecution::Examples::DataDrivenClassExample#0
                WEX::TestExecution::Examples::DataDrivenClassExample#0::Test1
                WEX::TestExecution::Examples::DataDrivenClassExample#0::Test2
            WEX::TestExecution::Examples::DataDrivenClassExample#1
                WEX::TestExecution::Examples::DataDrivenClassExample#1::Test1
                WEX::TestExecution::Examples::DataDrivenClassExample#1::Test2
            WEX::TestExecution::Examples::DataDrivenClassExample#2
                WEX::TestExecution::Examples::DataDrivenClassExample#2::Test1
                WEX::TestExecution::Examples::DataDrivenClassExample#2::Test2
            WEX::TestExecution::Examples::DataDrivenClassExample#3
                WEX::TestExecution::Examples::DataDrivenClassExample#3::Test1
                WEX::TestExecution::Examples::DataDrivenClassExample#3::Test2
```

### <span id="managed1_executing"></span><span id="MANAGED1_EXECUTING"></span>Managed

``` syntax
TE.exe Examples\CSharp.AdvancedDataDriven.Examples.dll /name:*class* /list
Test Authoring and Execution Framework v2.9.3k for x86

        F:\ Examples\CSharp.AdvancedDataDriven.Examples.dll
            WEX.Examples.CSharpDataDrivenClassExample#0
                WEX.Examples.CSharpDataDrivenClassExample#0.Test1
                WEX.Examples.CSharpDataDrivenClassExample#0.Test2
            WEX.Examples.CSharpDataDrivenClassExample#1
                WEX.Examples.CSharpDataDrivenClassExample#1.Test1
                WEX.Examples.CSharpDataDrivenClassExample#1.Test2
            WEX.Examples.CSharpDataDrivenClassExample#2
                WEX.Examples.CSharpDataDrivenClassExample#2.Test1
                WEX.Examples.CSharpDataDrivenClassExample#2.Test2
            WEX.Examples.CSharpDataDrivenClassExample#3
                WEX.Examples.CSharpDataDrivenClassExample#3.Test1
                WEX.Examples.CSharpDataDrivenClassExample#3.Test2
```

Notice that the indices in the examples above are similar to data-driven tests. Each row in the data-driven class is identified by an index. Just like in data-driven tests, **you could choose to give any row a more meaningful short *Name* by specifying the metadata at the Row level in the XML file and printing that name instead of the index when listing or executing the tests.**

Similarly, you use the **/listproperties** option to confirm that the data is indeed specified and available at the class level.

### <span id="native2_executing"></span><span id="NATIVE2_EXECUTING"></span>Native

``` syntax
F:\ Examples\CPP.AdvancedDataDriven.Examples.dll
    WEX::TestExecution::Examples::DataDrivenClassExample#0
            Property[DataSource] =  Table:DataDrivenClassExample.xml#ClassTable

            Data[Color] = White
            Data[Size] = 4
        WEX::TestExecution::Examples::DataDrivenClassExample#0::Test1
        WEX::TestExecution::Examples::DataDrivenClassExample#0::Test2

    WEX::TestExecution::Examples::DataDrivenClassExample#1
            Property[DataSource] =  Table:DataDrivenClassExample.xml#ClassTable

            Data[Color] = Black
            Data[Size] = 10
        WEX::TestExecution::Examples::DataDrivenClassExample#1::Test1
        WEX::TestExecution::Examples::DataDrivenClassExample#1::Test2

    WEX::TestExecution::Examples::DataDrivenClassExample#2
            Property[DataSource] =  Table:DataDrivenClassExample.xml#ClassTable

            Data[Color] = Orange
            Data[Size] = 9
        WEX::TestExecution::Examples::DataDrivenClassExample#2::Test1
        WEX::TestExecution::Examples::DataDrivenClassExample#2::Test2

    WEX::TestExecution::Examples::DataDrivenClassExample#3
            Property[DataSource] =  Table:DataDrivenClassExample.xml#ClassTable

            Data[Color] = Blue
            Data[Size] = 9
        WEX::TestExecution::Examples::DataDrivenClassExample#3::Test1
        WEX::TestExecution::Examples::DataDrivenClassExample#3::Test2
```

### <span id="managed2_executing"></span><span id="MANAGED2_EXECUTING"></span>Managed

``` syntax
F:\ Examples\CSharp.AdvancedDataDriven.Examples.dll
    WEX.Examples.CSharpDataDrivenClassExample#0
            Setup: MyClassInitialize
            Property[DataSource] =  Table:CSharpDataDrivenClassExample.xml#ClassTable

            Data[Color] = White
            Data[Size] = 4
        WEX.Examples.CSharpDataDrivenClassExample#0.Test1
        WEX.Examples.CSharpDataDrivenClassExample#0.Test2

    WEX.Examples.CSharpDataDrivenClassExample#1
            Setup: MyClassInitialize
            Property[DataSource] =  Table:CSharpDataDrivenClassExample.xml#ClassTable

            Data[Color] = Black
            Data[Size] = 10
        WEX.Examples.CSharpDataDrivenClassExample#1.Test1
        WEX.Examples.CSharpDataDrivenClassExample#1.Test2

    WEX.Examples.CSharpDataDrivenClassExample#2
            Setup: MyClassInitialize
            Property[DataSource] =  Table:CSharpDataDrivenClassExample.xml#ClassTable

            Data[Color] = Orange
            Data[Size] = 9
        WEX.Examples.CSharpDataDrivenClassExample#2.Test1
        WEX.Examples.CSharpDataDrivenClassExample#2.Test2

    WEX.Examples.CSharpDataDrivenClassExample#3
            Setup: MyClassInitialize
            Property[DataSource] =  Table:CSharpDataDrivenClassExample.xml#ClassTable

            Data[Color] = Blue
            Data[Size] = 9
        WEX.Examples.CSharpDataDrivenClassExample#3.Test1
        WEX.Examples.CSharpDataDrivenClassExample#3.Test2
```

You can apply all execution rules to the data-driven class. You can base your selection query on anything that you can list in the **/listproperties** option.

## <span id="ddtests_ddc"></span><span id="DDTESTS_DDC"></span>Data-driven tests in a Data-driven Class


You are not confined in any way fom having data-driven tests within a data-driven class. This approach can be useful when writing API tests. You can keep the common data for all tests in a class at the class level **DataSource**. You specify the data that is test method specific in the **DataSource** metadata for the method that you mark as data-driven.

NOTE: In such cases, the execution order is a little more involved.

The following examples show how the previous two example binaries render with the */list* command option.

### <span id="native1_ddtests"></span><span id="NATIVE1_DDTESTS"></span>Native

``` syntax
TE.exe Examples\CPP.AdvancedDataDriven.Examples.dll /name:*nested* /list
Test Authoring and Execution Framework v2.9.3k for x86

        F:\ Examples\CPP.AdvancedDataDriven.Examples.dll
            WEX::TestExecution::Examples::NestedDataDrivenExample#0
                WEX::TestExecution::Examples::NestedDataDrivenExample#0::Test1
                WEX::TestExecution::Examples::NestedDataDrivenExample#0::Test2#0
                WEX::TestExecution::Examples::NestedDataDrivenExample#0::Test2#1
                WEX::TestExecution::Examples::NestedDataDrivenExample#0::Test2#2
                WEX::TestExecution::Examples::NestedDataDrivenExample#0::Test2#3
            WEX::TestExecution::Examples::NestedDataDrivenExample#1
                WEX::TestExecution::Examples::NestedDataDrivenExample#1::Test1
                WEX::TestExecution::Examples::NestedDataDrivenExample#1::Test2#0
                WEX::TestExecution::Examples::NestedDataDrivenExample#1::Test2#1
                WEX::TestExecution::Examples::NestedDataDrivenExample#1::Test2#2
                WEX::TestExecution::Examples::NestedDataDrivenExample#1::Test2#3
            WEX::TestExecution::Examples::NestedDataDrivenExample#2
                WEX::TestExecution::Examples::NestedDataDrivenExample#2::Test1
                WEX::TestExecution::Examples::NestedDataDrivenExample#2::Test2#0
                WEX::TestExecution::Examples::NestedDataDrivenExample#2::Test2#1
                WEX::TestExecution::Examples::NestedDataDrivenExample#2::Test2#2
                WEX::TestExecution::Examples::NestedDataDrivenExample#2::Test2#3
            WEX::TestExecution::Examples::NestedDataDrivenExample#3
                WEX::TestExecution::Examples::NestedDataDrivenExample#3::Test1
                WEX::TestExecution::Examples::NestedDataDrivenExample#3::Test2#0
                WEX::TestExecution::Examples::NestedDataDrivenExample#3::Test2#1
                WEX::TestExecution::Examples::NestedDataDrivenExample#3::Test2#2
                WEX::TestExecution::Examples::NestedDataDrivenExample#3::Test2#3
```

### <span id="managed1_ddtests"></span><span id="MANAGED1_DDTESTS"></span>Managed

``` syntax
TE.exe Examples\CSharp.AdvancedDataDriven.Examples.dll /name:*nested* /list
Test Authoring and Execution Framework v2.9.3k for x86

        F:\ Examples\CSharp.AdvancedDataDriven.Examples.dll
            WEX.Examples.CSharpDataDrivenNestedExample#0
                WEX.Examples.CSharpDataDrivenNestedExample#0.Test1
                WEX.Examples.CSharpDataDrivenNestedExample#0.Test2#0
                WEX.Examples.CSharpDataDrivenNestedExample#0.Test2#1
                WEX.Examples.CSharpDataDrivenNestedExample#0.Test2#2
                WEX.Examples.CSharpDataDrivenNestedExample#0.Test2#3
            WEX.Examples.CSharpDataDrivenNestedExample#1
                WEX.Examples.CSharpDataDrivenNestedExample#1.Test1
                WEX.Examples.CSharpDataDrivenNestedExample#1.Test2#0
                WEX.Examples.CSharpDataDrivenNestedExample#1.Test2#1
                WEX.Examples.CSharpDataDrivenNestedExample#1.Test2#2
                WEX.Examples.CSharpDataDrivenNestedExample#1.Test2#3
            WEX.Examples.CSharpDataDrivenNestedExample#2
                WEX.Examples.CSharpDataDrivenNestedExample#2.Test1
                WEX.Examples.CSharpDataDrivenNestedExample#2.Test2#0
                WEX.Examples.CSharpDataDrivenNestedExample#2.Test2#1
                WEX.Examples.CSharpDataDrivenNestedExample#2.Test2#2
                WEX.Examples.CSharpDataDrivenNestedExample#2.Test2#3
            WEX.Examples.CSharpDataDrivenNestedExample#3
                WEX.Examples.CSharpDataDrivenNestedExample#3.Test1
                WEX.Examples.CSharpDataDrivenNestedExample#3.Test2#0
                WEX.Examples.CSharpDataDrivenNestedExample#3.Test2#1
                WEX.Examples.CSharpDataDrivenNestedExample#3.Test2#2
                WEX.Examples.CSharpDataDrivenNestedExample#3.Test2#3
```

**NOTE:** The only restriction in this case is that the tables for the two examples cannot be in the same **DataSource file**. In other words, the **DataSource** for the data-driven class and the data-driven test method that it contains must be different.

Notice that method **Test2** in our examples is a data-driven test within a data-driven class. For example, in the line **WEX.Examples.CSharpDataDrivenNestedExample\#3.Test2\#0**, **\#3** is the index for the class, and **\#0** is the index for the data-driven test within that class. **Test2** can access both tables: the data in the row of the class instance to which it belongs and the data in the current row for its own **DataSource** table. In other words, **the data at the class level and the data at the test method level are aggregated together and are available during the test method execution.**

What happens in the case of conflicting data - if the same data name is specified at both the class level and the method level? TAEF processes this condition in the same way that it processes metadata properties. **The data that is specified in a Row at the method level overrides the data that is specified in a Row at the class level.**

For example, consider the case when you have a parameter called **Size** that is specified both at the class level and at the test method level. At the class level, **Size** is defined to be of *String Array* type, but at the test method level, it is defined to be an *int*. In this case, the *int* type overrides the *String Array* type at the test method level, as well as at the **Setup** and **Teardown** methods for the test. However at the **Setup** and **Teardown** methods at the class level, **Size** has the *String Array* data type.

If you have any such conflicting data in your code, TAEF shows a warning during execution and lists the properties, but the conflicting data will not result in any failure.

 

 





