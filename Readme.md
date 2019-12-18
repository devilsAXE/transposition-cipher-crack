<h2> Codebreaking </h2> 
<p align="justify"> In this programming assignment you are supposed to write a CRACK i.e the code that takes ciphertext as input and produces the
corresponding plaintext without knowing the key for the ciphertext provided to it.</p>
<h4>About the Encryption Scheme</h4>
<p>
The plaintext contains usual English paragraphs. The key contains only capital letters. To encrypt a small letter, it is first converted
to its corresponding capital letter, which is then encrypted as capital letter, and finally the encrypted capital letter is converted back
to corresponding small letter. So, in ciphertext, a small letter corresponds to a small letter in plaintext and same for capital letter.
The special characters (characters other than alphabet) are copied as it is in the ciphertext from the plaintext. However, the spaces
from the paragraph have been removed. So, it does not matter whether we give spaces between the words in the plaintext or remove
it. An example to demonstrate the process of encryption is given here.
</p>
<h5>Plaintext:</h5>
<code>One day a college professor after getting irritated in his college class stands up in front of the class and asks if anyone in
the class is an idiot, and if there is one then he/she should stand up. After a minute a young man stands up. The professor
then asks that guy if he actually thinks he is an idiot. The boy replied, "No, I just didn't want to see you standing there all
by yourself."
</code>
<h5>Ciphertext:</h5>
<code>krfkigkhudkgihrkgifjwmlsogmaolgoqwjldksnjgodlfkigjnalgnloriwqlfksnvjoidjtifklsangkodlcmgkieksauvglojqmldkoelan
ldmksislo,fklsofjtoglasjvmkgorw/edpgldkgnotaldkscmgkoegldjm. ... ciphertext cont..........
Notice the presence of symbols “,”, “/” and “.” in the ciphertex
</code>

<h5>Usage</h5>
<p align="justify"> 
The FinalCrack.py has two modes:
<ul>
  <li><b>Encryption Mode</b>
  </br>The <code>encrpyt</code> mode allows encryption of a english text file as per the aforementioned rule. Following is the usage :</br>
<b><code>python FinalCrack.py encrypt &lt;key&gt; &lt;filepath&gt; </code></b>
  </li>
  <li><b>Crack Mode </b>
 </br>The <code>crack</code> mode allows producing an approximate <b>key</b> as well as the plaintext generated using that key. Following is the usage :</br>
<b><code>python FinalCrack.py crack &lt;filepath&gt; </code></b>
  </li>
</ul>
</p>
