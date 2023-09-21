from Crypto.Util.number import long_to_bytes
n = 31091873146151684702346697466440613735531637654275447575291598179592628060572504006592135492973043411815280891993199034777719870850799089897168085047048378272819058803065113379019008507510986769455940142811531136852870338791250795366205893855348781371512284111378891370478371411301254489215000780458922500687478483283322613251724695102723186321742517119591901360757969517310504966575430365399690954997486594218980759733095291730584373437650522970915694757258900454543353223174171853107240771137143529755378972874283257666907453865488035224546093536708315002894545985583989999371144395769770808331516837626499129978673
e = 65537
c = 8684906481438508573968896111659984335865272165432265041057101157430256966786557751789191602935468100847192376663008622284826181320172683198164506759845864516469802014329598451852239038384416618987741292207766327548154266633297700915040296215377667970132408099403332011754465837054374292852328207923589678536677872566937644721634580238023851454550310188983635594839900790613037364784226067124711011860626624755116537552485825032787844602819348195953433376940798931002512240466327027245293290482539610349984475078766298749218537656506613924572126356742596543967759702604297374075452829941316449560673537151923549844071
s = 352657755607663100038622776859029499529417617019439696287530095700910959137402713559381875825340037254723667371717152486958935653311880986170756144651263966436545612682410692937049160751729509952242950101025748701560375826993882594934424780117827552101647884709187711590428804826054603956840883672204048820926
l = n - s + 1
d = pow(e, -1, l)
m = pow(c, d, n)
print(long_to_bytes(m).decode())
