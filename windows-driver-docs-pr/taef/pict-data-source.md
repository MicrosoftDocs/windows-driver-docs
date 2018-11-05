---
title: PICT Data Source
description: PICT Data Source
ms.assetid: 75D3E086-C277-410d-B474-742A47ABB6AC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PICT Data Source


Please make sure that you are familiar with basic execution of TAEF and know how to Author Tests using it, before proceeding with this section.

## <span id="PICT_Background_and_References"></span><span id="pict_background_and_references"></span><span id="PICT_BACKGROUND_AND_REFERENCES"></span>PICT Background and References


PICT stands for Pairwise Independent Combinatorial Testing. **PICT allows you to specify variations for each of your parameter separately.** For example, if the API test depends on two parameters: FileName and FileExtension, you could think of the possible variations to pass for FileName and for FileExtensions separately like so:

-   FileName: a, z12390, Realllyreallyreallylonglonglonglonglonglonglonglonglonglong, normallength
-   FileExtension: txt, png, bat, doc, exe, bmp, wav

Now, you can see that a **brute-force combinatorial expansion** of the above (4 X 7 = 28) **could easily get out of bounds** as you think of more variations to add to the list. In such test case scenarios, **PICT could add a lot of value by generating a compact set of parameter results to get comprehensive combinatorial coverage over the input parameters.**

## <span id="PICT_Support_in_TAEF"></span><span id="pict_support_in_taef"></span><span id="PICT_SUPPORT_IN_TAEF"></span>PICT Support in TAEF


TAEF offers in-built support for PICT based tests.

To take advantage of this, write your input model file for pict.exe as you would normally. Refer to the \*.txt files in the examples folder mentioned above. It might be useful to try if PICT executes as expected on your model file by trying it at the command prompt first like so:

``` syntax
pict.exe <model file> [/e:<seed file>]
```

Pict.exe is available with the rest of the binaries on TAEF's latest release share.

One you are done authoring your model file (and seed file) for PICT and have verified it against pict.exe at the command prompt, you can now mark up your tests to let TAEF know that they are PICT driven tests. If you are familiar with table based data-driven testing available in TAEF, you will find this very similar.

Native code:

```cpp
1     class PictExample
2     {
3         TEST_CLASS(PictExample)
4
5         BEGIN_TEST_METHOD(SimpleTest)
6             TEST_METHOD_PROPERTY(L"DataSource", L"pict:PictExample.txt")
7         END_TEST_METHOD()
8
9         BEGIN_TEST_METHOD(TestWithSeed)
10            TEST_METHOD_PROPERTY(L"DataSource", L"pict:TestWithSeed.txt")
11            TEST_METHOD_PROPERTY(L"Pict:SeedingFile", L"TestWithSeed.sed")
12            TEST_METHOD_PROPERTY(L"Pict:Timeout", L"00:01:30")
13        END_TEST_METHOD()
14
15        BEGIN_TEST_METHOD(TestWithFunction)
16            TEST_METHOD_PROPERTY(L"DataSource", L"pict:TestWithFunction.txt")
17        END_TEST_METHOD()
18    };
```

Managed code:

```cpp
1     [TestClass]
2     public class CSharpPictExample
3     {
4         [TestMethod]
5         [DataSource("pict:ConstraintsTest.txt")]
6         [TestProperty("Pict:SeedingFile", "ConstraintsTest.seed")]
7         public void ConstraintsTest()
8         {
9             ...
10        }
11
12        [TestMethod]
13        [DataSource("pict:SumofSquareRoots.txt")]
14        public void SumOfSquareRoots()
15        {
16            ...
17        }
18
19        public TestContext TestContext
20        {
21            get { return m_testContext; }
22            set { m_testContext = value; }
23        }
24
25        private TestContext m_testContext;
26    }
```

As shown in the above examples, you need to specify the name of the model file as the DataSource. **You must prefix the name of the model file with "pict:"** and provide this as the DataSource for your test method. In case of the managed test, just like with any other data-driven test with TAEF, you must provide TestContext property get and set methods and have a private instance of the same in your class.

If you want to pass command options to PICT, you can use metadata for this purpose. Use the following table to map the command options of Pict.exe to TAEF metadata.


| pict.exe command syntax |                Native TAEF metadata syntax                |           Managed TAEF metadata syntax            |
|-------------------------|-----------------------------------------------------------|---------------------------------------------------|
|          /o:3           |        TEST\_METHOD\_PROPERTY(L"Pict:Order", L"3")        |        \[TestProperty("Pict:Order", "3")\]        |
|          /d:,           |   TEST\_METHOD\_PROPERTY(L"Pict:ValueSeparator", L",")    |   \[TestProperty("Pict:ValueSeparator", ",")\]    |
|           /a:           |                                                           | TEST\_METHOD\_PROPERTY(L"Pict:AliasSeparator", L" |
|          /n:~           | TEST\_METHOD\_PROPERTY(L"Pict:NegativeValuePrefix", L"~") | \[TestProperty("Pict:NegativeValuePrefix", "~")\] |
|      /e:test.seed       | TEST\_METHOD\_PROPERTY(L"Pict:SeedingFile", L"test.seed") | \[TestProperty("Pict:SeedingFile", "test.seed")\] |
|           /r            |      TEST\_METHOD\_PROPERTY(L"Pict:Random", L"true")      |      \[TestProperty("Pict:Random", "true")\]      |
|          /r:33          |     TEST\_METHOD\_PROPERTY(L"Pict:RandomSeed", L"33")     |     \[TestProperty("Pict:RandomSeed", "33")\]     |
|           /c            |  TEST\_METHOD\_PROPERTY(L"Pict:CaseSensitive", L"true")   |  \[TestProperty("Pict:CaseSensitive", "true")\]   |

Any of the above metadata can be set at the command prompt, in the DataSource property, or as test, class, or module level metadata, with precedence in that order. To set it at the command prompt, use the syntax:

``` syntax
te.exe <test dll> /Pict:Order=3 /Pict:SeedingFile=test.seed
```

To set metadata in the DataSource property, append the model file name with a question mark character (?) then a set of ampersand-separated metadata name = metadata value pairs. When using this method, the "Pict:" prefix for metadata names is optional. Here is an example:

```cpp
TEST_METHOD_PROPERTY(L"DataSource", L"Pict:model.txt?Order=3&CaseSensitive=true&Random=true")
```

Behind the scenes, TAEF will supply your input model file and command options to PICT and get the results. If PICT produces any errors or warnings, you will see these logged as warnings by TAEF. For each resultant output row that PICT produces, TAEF will re-invoke the test in concern.

Setting the "Pict:RandomSeed" value will change the default for "Pict:Random" from false to true. This way, you can explicitly set "Pict:Random" to false to get TAEF to ignore "Pict:RandomSeed".

**The default time-out allowed for PICT.exe to execute on the model file and seed file input specified is 5 minutes.** If your model file is more involved and needs more time than 5 minutes for PICT.exe to return results, you can override this time out as shown in the CPP example above by specifying the **"Pict:Timeout"** metadata. In the example, a 1.5 minute time-out is specified via the standard [TAEF Time-out](taef-timeouts.md) format. Like the other PICT metadata, the "Pict:Timeout" metadata is inherited and hence can be specified for the whole class or module.

You can access the data values during a given invocation from your test method and its associated setup and cleanup methods in the same way as you did for table based data-driven tests with TAEF - using the TestData class for native code and using the TestContext for managed code like so:

Native code:

```cpp
1     void PictExample::SimpleTest()
2     {
3         String valueA;
4         if (SUCCEEDED(TestData::TryGetValue(L"A", valueA)))
5         {
6           Log::Comment(L"A retrieved was " + valueA);
7         }
8
9         String valueB;
10        if (SUCCEEDED(TestData::TryGetValue(L"B", valueB)))
11        {
12            Log::Comment(L"B retrieved was " + valueB);
13        }
14
15        String valueC;
16        if (SUCCEEDED(TestData::TryGetValue(L"C", valueC)))
17        {
18            Log::Comment(L"C retrieved was " + valueC);
19        }
20
21        unsigned int index;
22        if (SUCCEEDED(TestData::TryGetValue(L"index", index)))
23        {
24            Log::Comment(String().Format(L"At index %d", index));
25        }
26    }
```

Managed code:

```cpp
1      [TestClass]
2      public class CSharpPictExample
3      {
4          [TestMethod]
5          [DataSource("pict:ConstraintsTest.txt")]
6          public void ConstraintsTest()
7          {
8              Log.Comment("A is " + m_testContext.DataRow["A"]);
9              Log.Comment("B is " + m_testContext.DataRow["B"]);
10             Log.Comment("C is " + m_testContext.DataRow["C"]);
11             Log.Comment("D is " + m_testContext.DataRow["D"]);
12
13             UInt32 index = (UInt32)m_testContext.DataRow["Index"];
14             Log.Comment("At index " + index.ToString());
15        }
16
17        [TestMethod]
18        [DataSource("pict:SumofSquareRoots.txt")]
19        public void SumOfSquareRoots()
20        {
21             Log.Comment("A is " + m_testContext.DataRow["A"]);
22             Log.Comment("B is " + m_testContext.DataRow["B"]);
23
24             UInt32 index = (UInt32)m_testContext.DataRow["Index"];
25             Log.Comment("At index " + index.ToString());
26        }
27
28        public TestContext TestContext
29        {
30             get { return m_testContext; }
31             set { m_testContext = value; }
32        }
33
34        private TestContext m_testContext;
35    }
```

Just like with any data-driven tests in TAEF, "Index" is reserved and should not be used as parameter name. Index implicitly refers to the index of the test method invocation and is accessible from the test method if your test needs it.

**It is also important to note that in case of PICT based tests, the datatype for all parameters is assumed to be WEX::Common::String (native), String(managed) or VT\_BSTR(script).** The conversion and interpretation is left up to the user.

Now that you are done with authoring the PICT based test using TAEF, you can invoke it from the command prompt and apply all of the command features that TAEF offers to it: like **/list** to get a list of all test methods that will get generated using the PICT output as data, **/listproperties** to get a list of the test method names along with the metadata and data values that they are associated with etc. The key thing to **note before you start is to ensure that pict.exe is in your path.**

Here are a few examples:

``` syntax
te Examples\CPP.Pict.Example.dll /list /name:*SimpleTest*
Test Authoring and Execution Framework v2.9.3k for x86
        f:\ Examples\CPP.Pict.Example.dll
            WEX::TestExecution::Examples::PictExample
                WEX::TestExecution::Examples::PictExample::SimpleTest#0
                WEX::TestExecution::Examples::PictExample::SimpleTest#1
                WEX::TestExecution::Examples::PictExample::SimpleTest#2
                WEX::TestExecution::Examples::PictExample::SimpleTest#3
                WEX::TestExecution::Examples::PictExample::SimpleTest#4
                WEX::TestExecution::Examples::PictExample::SimpleTest#5
                WEX::TestExecution::Examples::PictExample::SimpleTest#6
                WEX::TestExecution::Examples::PictExample::SimpleTest#7
                WEX::TestExecution::Examples::PictExample::SimpleTest#8
                WEX::TestExecution::Examples::PictExample::SimpleTest#9
                WEX::TestExecution::Examples::PictExample::SimpleTest#10
                WEX::TestExecution::Examples::PictExample::SimpleTest#11
                WEX::TestExecution::Examples::PictExample::SimpleTest#12
                WEX::TestExecution::Examples::PictExample::SimpleTest#13
                WEX::TestExecution::Examples::PictExample::SimpleTest#14
                WEX::TestExecution::Examples::PictExample::SimpleTest#15
                WEX::TestExecution::Examples::PictExample::SimpleTest#16
                WEX::TestExecution::Examples::PictExample::SimpleTest#17
                WEX::TestExecution::Examples::PictExample::SimpleTest#18
                WEX::TestExecution::Examples::PictExample::SimpleTest#19
                WEX::TestExecution::Examples::PictExample::SimpleTest#20
                WEX::TestExecution::Examples::PictExample::SimpleTest#21
                WEX::TestExecution::Examples::PictExample::SimpleTest#22
                WEX::TestExecution::Examples::PictExample::SimpleTest#23
```

To read more about selection criteria (/select and /name) please refer to the Selection wiki page.

``` syntax
te Examples\Csharp.Pict.Example.dll /listproperties /select:"@Name='*SumofSquare*'
                    and @Data:index>10
Test Authoring and Execution Framework v2.9.3k for x86
        f:\ Examples\CSharp.Pict.Example.dll
            WEX.Examples.CSharpPictExample
                WEX.Examples.CSharpPictExample.SumOfSquareRoots#11
                        Property[DataSource] = pict:SumofSquareRoots.txt
                        Data[a] = 1
                        Data[b] = ~-1
                WEX.Examples.CSharpPictExample.SumOfSquareRoots#12
                        Property[DataSource] = pict:SumofSquareRoots.txt
                        Data[a] = 2
                        Data[b] = ~-1
```

The above example shows how you can select using the index. You may also choose to select based on the data value.

``` syntax
te Examples\Csharp.Pict.Example.dll /listproperties /select:"@Name='*SumofSquare*'
                    and (@Data:A='1' and @Data:B='1')"
Test Authoring and Execution Framework v2.9.3k for x86
        f:\ Examples\CSharp.Pict.Example.dll
            WEX.Examples.CSharpPictExample
                WEX.Examples.CSharpPictExample.SumOfSquareRoots#8
                        Property[DataSource] = pict:SumofSquareRoots.txt
                        Data[a] = 1
                        Data[b] = 1
```

## <span id="PICT_Result_Caching"></span><span id="pict_result_caching"></span><span id="PICT_RESULT_CACHING"></span>PICT Result Caching


Some model file may get very complex and might require longer time to get processed by Pict.exe. TAEF tries to mitigate processing time for results by caching results during a given execution of Te.exe. If a subsequent test in the same execution run refers to the same model and seed file combination, TAEF will use the cached results. By default, at the end of each execution the cached results get deleted.

If you want to continue to take advantage of the cached results in subsequent runs, you could specify the "/persistPictResults" option at the command prompt during execution. Whenever you specify "/persistPictResults" for your command, the first execution will actually execute pict.exe and may take a long time, but all subsequent runs will use the cached results in cases where the model and seed file have been unmodified. **Note: You will need to continue specifying "/persistPictResults" for subsequent runs. Any subsequent run where you don't specify it will delete the cached results at the end of that run.**

If persisting the PICT results, and using cached data is something you want to do by default, you may set it as part of your te\_cmd environment variable as shown below and eliminate the need to specify it on every run. See [Executing Tests](executing-tests.md) for more details on te\_cmd.

``` syntax
set te_cmd = /persistPictResults
```

The cached result files are stored in a folder called "TAEF-PICT" in %temp% directory, if Te.exe has access to it, or in the current execution directory from where Te.exe was launched. The only time you may have the results in an inconsistent state is if you hit Ctrl + C during execution. In such a case, TAEF will attempt to delete the cached results, but if it is unable to do so, you will see an error to the effect. The error will prompt you to delete the cached results location. Failing to do may result in undefined or erroneous behaviour in subsequent tests.

With in-built PICT support in TAEF, you can now make the most of both, features in PICT as well as features in TAEF in your test automation.

## <span id="DataSource_as_a_Resource"></span><span id="datasource_as_a_resource"></span><span id="DATASOURCE_AS_A_RESOURCE"></span>DataSource as a Resource


You can add PICT models and seeding files as resources in your test module.

In native code, this is done by specifying the resource name instead of the file name in the DataSource metadata. Here is an example:

```cpp
BEGIN_TEST_METHOD(ResourceNameDataSource)
    TEST_METHOD_PROPERTY(L"DataSource", L"Pict:MyModelResourceName?SeedingFile=MySeedingResourceName")
END_TEST_METHOD()
```

"MyModelResourceName" and "MySeedingResourceName" are the resource names defined in a .rc file. The resource type needs to be DATAFILE, unlike in [table data sources](table-data-source.md) where the resource type needs to be DATASOURCE\_XML.

```cpp
MyModelResourceName DATAFILE "model.txt"
MySeedingResourceName DATAFILE "seed.txt"
```

The DataSource metadata value will remain the same as it did when the model was a file. Likewise in native code, you could make the resource name be the same as the file name. TAEF will first look for the presence of the actual file with the DataSource name. If the file is not found, it proceed by looking in the test module's resources. Since changing the DataSource stored in the resource requires recompiling, you can leverage this design by copying over the DataSource file to the same location as the test dll while developing (and naming the resource name to be the same as the file name). Once you are done testing, move (not copy) the file back to the code directory and recompile to embed the resource.









