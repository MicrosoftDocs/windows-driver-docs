---
title: Data-driven Testing in Scripting Languages
description: Data-driven Testing in Scripting Languages
ms.assetid: CF60C594-8877-4f09-AF82-9F4CA27123C7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# <span id="taef.data-driven_testing_in_scripting_languages"></span>Data-driven Testing in Scripting Languages


In order to understand this section, you should be familiar with how to [author tests in scripting languages](authoring-tests-in-scripting-languages.md). This section won't discuss details of the [various TAEF data-driven testing approaches](data-driven-testing.md). For a quick overview, review the different TAEF data-driven testing constructs:

-   [Table based data-driven testing](table-data-source.md)
-   [WMI Based data-driven testing](wmi-data-source.md)
-   [PICT based data-driven testing](pict-data-source.md)
-   [Light-weight data-driven testing](light-weight-data-driven-testing.md)

You may even choose to have a combination of data sources by having one or more data sources of any of the above. See [Specifying Multiple DataSources](multiple-datasources.md) for details.

## <span id="Specifying_the_data_source_in_scripting_language"></span><span id="specifying_the_data_source_in_scripting_language"></span><span id="SPECIFYING_THE_DATA_SOURCE_IN_SCRIPTING_LANGUAGE"></span>Specifying the data source in scripting language


Data-driven testing in TAEF allows you to specify the **DataSource** at the class or test level. In a data-driven class, the data is available to class and test method setup, cleanup, and all the test methods in the class. The **DataSource** parameter is the information that tells where the data will be retrieved from. In the case of table-based data-driven tests, this value includes the relative path to the XML file and the TableId in the XML file where the data is located. See the links that are listed above for more details.

The following example shows how to specify the **DataSource** property.

```cpp
1   <?xml version="1.0" ?>
2   <?component error="true" debug="true"?>
3   <package>
4       <component id="VBSampleTests">
5           <object id="Log" progid="WEX.Logger.Log" />
6           <object id="TestData" progid="Te.Common.TestData" />
7
8           <public>
9               <method name="TestOne">
10                  <TestMethodProperty name="DataSource" value="WMI:SELECT Label, Caption FROM Win32_Volume"/>
11              </method>
12
13              <method name="TestTwo">
14                  <TestMethodProperty name="DataSource" value="Table:ScriptExampleTable.xml#MyTable;WMI:SELECT Label, Caption FROM Win32_Volume"/>
15              </method>
16          </public>
17
18          <script language="VBScript">
19              <![CDATA[
20                  Function TestOne()
21                      dim caption
22                      caption = "NoCaption"
23                      Log.Comment("Caption is " + caption)
24
25                      If TestData.Contains("Caption") Then
26                      caption = TestData.GetValue("Caption")
27                      End If
28                      Log.Comment("Caption is " + caption)
29                  End Function
30
31                  Function TestTwo()
32                      Log.Comment("Calling TestTwo")
33                      dim caption
34                      caption = "NoCaption"
35                      Log.Comment("Caption is " + caption)
36
37                      If TestData.Contains("Caption") Then
38                      caption = TestData.GetValue("Caption")
39                      End If
40                      Log.Comment("Caption is " + caption)
41
42                      dim size
43                      If TestData.Contains("Size") Then
44                      size = TestData.GetValue("Size")
45                      End If
46                      Log.Comment("Size is " + CStr(size))
47
48                      dim transparency
49                      If TestData.Contains("Transparency") Then
50                      transparency = TestData.GetValue("Transparency")
51                      End If
52                      Log.Comment("Transparency is " + CStr(transparency))
53                  End Function
54              ]] >
55          </script>
56      </component>
57
58      <component id="JScriptSampleTests">
59          <object id="Log" progid="WEX.Logger.Log" />
60          <object id="TestData" progid="Te.Common.TestData" />
61
62          <TestClassProperty name="DataSource" value="Table:ScriptExampleTable.xml#MyTable"/>
63
64          <public>
65              <method name="ClassSetup" type="TestClassSetup"/>
66              <method name="ClassCleanup" type="TestClassCleanup"/>
67              <method name="MethodSetup"  type="TestMethodSetup"/>
68              <method name="MethodCleanup" type="TestMethodCleanup"/>
69
70              <method name="TestOne"/>
71              <method name="TestTwo">
72                  <TestMethodProperty name="DataSource" value="WMI:SELECT Label, Caption FROM Win32_Volume"/>
73              </method>
74          </public>
75
76          <script language="JScript">
77              <![CDATA[
78                  function ClassSetup()
79                  {
80                      Log.Comment("Calling class setup");
81                      var size;
82                      if(TestData.Contains("Size"))
83                      {
84                          size = TestData.GetValue("Size");
85                      }
86                      Log.Comment("Size is " + size);
87  
88                      var transparency;
89                      if(TestData.Contains("Transparency"))
90                      {
91                          transparency = TestData.GetValue("Transparency");
92                      }
93                      Log.Comment("Transparency is " + transparency);
94                  }
95
96                  function ClassCleanup()
97                  {
98                      Log.Comment("Calling class cleanup");
99                      return true;
100                 }
101
102                 function MethodSetup()
103                 {
104                     Log.Comment("Calling method setup");
105                     var size;
106                     if(TestData.Contains("Size"))
107                     {
108                         size = TestData.GetValue("Size");
109                     }
110                     Log.Comment("Size is " + size);
111
112                     var transparency;
113                     if(TestData.Contains("Transparency"))
114                     {
115                         transparency = TestData.GetValue("Transparency");
116                     }
117                     Log.Comment("Transparency is " + transparency);
118                     return true;
119                 }
120
121                 function MethodCleanup()
122                 {
123                     Log.Comment("Calling method cleanup");
124                     return true;
125                 }
126
127                 function TestOne()
128                 {
129                     Log.Comment("Calling TestOne");
130                     var size;
131                     if(TestData.Contains("Size"))
132                     {
133                         size = TestData.GetValue("Size");
134                     }
135                     Log.Comment("Size is " + size);
136
137                     var transparency;
138                     if(TestData.Contains("Transparency"))
139                     {
140                         transparency = TestData.GetValue("Transparency");
141                     }
142                     Log.Comment("Transparency is " + transparency);
143                 }
144
145                 function TestTwo()
146                 {
147                     Log.Comment("Calling TestTwo");
148                     var caption = "NoCaption";
149                     Log.Comment("Initial caption: " + caption);
150
151                     if(TestData.Contains("Caption"))
152                     {
153                         caption = TestData.GetValue("Caption");
154                     }
155                     Log.Comment("Caption is " + caption);
156
157                     var size;
158                     if(TestData.Contains("Size"))
159                     {
160                         size = TestData.GetValue("Size");
161                     }
162                     Log.Comment("Size is " + size);
163
164                     var transparency;
165                     if(TestData.Contains("Transparency"))
166                     {
167                         transparency = TestData.GetValue("Transparency");
168                     }
169                     Log.Comment("Transparency is " + transparency);
170                 }
171             ]] >
172         </script>
173     </component>
174 </package>
```

In the example above, lines 6 and 60 declare and instantiate a **TestData** object that allows access to the data for the data-driven tests.

The **&lt;TestMethodProperty&gt;** and **&lt;TestClassProperty&gt;** tags are lines that define **DataSource** for the test or class. In the VBSampleTests, **TestOne** has a [WMI query](wmi-data-source.md) as its **DataSource**. The parameters **label** and **caption** are available to **TestOne's** setup, cleanup, and test methods. In the same class, **TestTwo** has [Multiple DataSources](multiple-datasources.md) defined. The first is a [Table based DataSource](table-data-source.md), and the second is the same WMI based **DataSource** as **TestOne**.

TAEF generates a combinatorial expansion of the parameter sets for each of the **DataSource** properties. One parameter set is available for each test method invocation. If the WMI query returns four sets of results (Win32\_Volume) and there are three rows in the table based **DataSource**, **TestOne** will execute four times - once with each Win32\_Volume that the WMI query returns. On the other hand, **TestTwo** executes 12 (4 X 3) times for each combination of Win32\_Volume data and Row that the table specifies. The data is also available to the associated setup and cleanup methods.

In the JScriptSampleTests, you can see an example of a data-driven class. Because the example specifies **DataSource** at the class level, the data is available to all of the test methods - as well as the test and class level setup and cleanup methods. Because **TestTwo** is a data-driven test within a data-driven class, the data from the **DataSource** at the class level as well as that from the test level is available for **TestTwo**.

## <span id="Data_types_available_for_script_tests"></span><span id="data_types_available_for_script_tests"></span><span id="DATA_TYPES_AVAILABLE_FOR_SCRIPT_TESTS"></span>Data types available for script tests


The following parameter types are available for scripting languages. These are the types that you can specify in table based data-driven testing. The default parameter type is *String* or *BSTR* (representing *VT\_BSTR*).

The section [Parameter Types in Table based DataSource](parameter-types-in-table-data-sources.md) shows how to view the available parameter types (in Native and Managed code) while authoring tests in a scripting language.

## <span id="Executing_data-driven_scripts"></span><span id="executing_data-driven_scripts"></span><span id="EXECUTING_DATA-DRIVEN_SCRIPTS"></span>Executing data-driven scripts


The **/listproperties** option lists not only the metadata but also the data that is available for each invocation of the test. (Running the **/listproperties** option on the entire dll is left as an exercise to the reader.) The following example selects the invocation of **TestOne** from VBSampleTests using the [selection query](selection.md) language:

``` syntax
f:\spartadev.binaries.x86chk\WexTest\CuE\TestExecution>te Examples\DataDrivenTest.wsc /listproperties /name:VBSampleTests::TestOne*

Test Authoring and Execution Framework v.R10 Build 6.1.6939.0 For x86

        f:\spartadev.binaries.x86chk\WexTest\CuE\TestExecution\Examples\DataDrivenTest.wsc
            VBSampleTests
                VBSampleTests::TestOne#0
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = C:\
                        Data[Label] =

                VBSampleTests::TestOne#1
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = D:\
                        Data[Label] = New Volume

                VBSampleTests::TestOne#2
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = F:\
                        Data[Label] = New Volume

                VBSampleTests::TestOne#3
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = E:\
                        Data[Label] = New Volume

                VBSampleTests::TestOne#4
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = G:\
                        Data[Label] = New Volume

                VBSampleTests::TestOne#5
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = H:\
                        Data[Label] = New Volume

                VBSampleTests::TestOne#6
                        Property[DataSource] = WMI:SELECT Label, Caption FROM Win32_Volume

                        Data[Caption] = K:\
                        Data[Label] =
```

The **/listproperties** option shows that TAEF invoked the test method **VBSampleTests::TestOne** 7 times - once for each Win32\_Volume. For each invocation, TAEF appends an implicit *index* to the test method to distinguish each invocation. You can also see the data and metadata that is available for each invocation of the test method.

Using the information from the **/listproperties** option, you can apply a selection query that is based on the data value or the index value to gain finer control of which test invocations to execute. The following example shows how to run only the invocation where the caption is **E:\\**:

``` syntax
te Examples\DataDrivenTest.wsc /select:"@Name='VBSampleTests::TestOne*' and @Data:Caption='E:\'"
```

The following command uses the index to select the same test:

``` syntax
te Examples\DataDrivenTest.wsc /select:"@Name='VBSampleTests::TestOne*' and @Data:Index=3"
```

Using PICT based and light weight data-driven tests in a script test is left as an exercise to the reader.

 

 





