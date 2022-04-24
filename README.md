# graduation-thesis-code
基于股权激励事件的因子选股多头策略，学位论文的代码部分，可下载使用，谢绝转载

<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">库名</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">版本号</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">python<o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">3.9.7<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">numpy</span></span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">1.21.4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">pandas<o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">1.3.4<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">re<o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">2.2.1<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">matplotlib<o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">3.4.3<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">statsmodels</span></span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">0.13.1<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;mso-yfti-lastrow:yes">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span class="SpellE"><span lang="EN-US">scipy</span></span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
  <td width="73" style="width:54.45pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span lang="EN-US">1.7.2<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>


<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="604" style="width:453.05pt;border-collapse:collapse;border:none;mso-border-alt:
 solid windowtext .5pt;mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes">
  <td width="115" style="width:86.35pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">文件名</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
  <td width="489" style="width:366.7pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">主要模块与功能</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1">
  <td width="115" rowspan="4" style="width:86.35pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">数据预处理最终提交版</span><span lang="EN-US">.<span class="SpellE">ipynb</span><o:p></o:p></span></p>
  </td>
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">获取股权激励基本信息数据，进行正文中提到的数据处理操作并构造因子，将处理后的数据保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2">
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">获取股权激励文本数据，进行正文中提到的数据处理操作并构造因子，将处理后的数据保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3">
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">获取股权激励比例数据，进行正文中提到的数据处理操作并构造因子，将处理后的数据保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4">
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">获取财务和价量数据，进行正文中提到的数据处理操作并构造因子，将处理后的数据保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5">
  <td width="115" rowspan="3" style="width:86.35pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6" align="center" style="text-align:center"><span style="font-family:
  宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;mso-hansi-font-family:&quot;Times New Roman&quot;">正式问题最终提交版</span><span lang="EN-US">.<span class="SpellE">ipynb</span><o:p></o:p></span></p>
  </td>
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">执行事件研究法，将结果进行展示并保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6">
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">执行描述性统计和单因子测试，将结果进行展示并保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;mso-yfti-lastrow:yes">
  <td width="489" style="width:366.7pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="6"><span style="font-family:宋体;mso-ascii-font-family:&quot;Times New Roman&quot;;
  mso-hansi-font-family:&quot;Times New Roman&quot;">执行选股回测，将结果进行展示并保存到本地。</span><span lang="EN-US"><o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>
