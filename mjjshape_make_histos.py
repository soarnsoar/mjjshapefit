import ROOT
Year='2018'

f_input="../"+Year+"/rootFile_"+Year+"__cms_scratch_jhchoi_MjjShape_Resolved_HMFull_V13_RelW0.02_DeepAK8WP0p5_dMchi2Resolution_Combine/hadd.root"
histodir='___ResolvedALL__SB_NoMEKDCut/HadronicW_mass/'
nonwjet_bkglist=['ZHWWlnuqq_M125',
                 'tW',
                 'qqWWqq',
                 'WW',
                 'ggWW',
                 'ggH_hww',
                 'MultiBoson',
                 'QCD',
                 'DY',
                 'qqH_hww',
                 'TT',
                 'SingleTop',
                 'WpHWWlnuqq_M125',
                 'WmHWWlnuqq_M125',]

Wjets=['Wjets0j','Wjets1j','Wjets2j']

idx=0

mytfile=ROOT.TFile.Open(f_input)
for b in nonwjet_bkglist:
    if idx==0:
        hbkg=mytfile.Get(histodir+"/histo_"+b).Clone()
    else:
        htemp=mytfile.Get(histodir+"/histo_"+b).Clone()
        hbkg.Add(htemp)
    idx+=1
hbkg.SetTitle('bkg')
hbkg.SetName('bkg')


##--wjets
idx=0
for w in Wjets:
    if idx==0:
        hwjets=mytfile.Get(histodir+'/histo_'+w).Clone()
    else:
        htemp=mytfile.Get(histodir+"/histo_"+w).Clone()
        hwjets.Add(htemp)
    idx+=1
##--data
hdata=mytfile.Get(histodir+'/histo_DATA').Clone()


##--data - nonwjet_bkg

hdata_onlywjets=hdata.Clone()
hdata_onlywjets.Add(hbkg,-1)




c=ROOT.TCanvas()
hdata_onlywjets.Draw()
#hwjets.Draw('same')
#hwjets.SetLineColor(3)
#c.SaveAs('temp.pdf')

hratio_onlywjets=hdata_onlywjets.Clone()
hratio_onlywjets.Divide(hwjets)
hratio_onlywjets.Draw()
#c.SaveAs('temp.pdf')

hratio_onlywjets.SetTitle('HadronicW_mass ratio')
hratio_onlywjets.SetName('HadronicW_mass ratio')
hratio_onlywjets.SetMaximum(1.5)
hratio_onlywjets.SetMinimum(0.5)


newtfile=ROOT.TFile('output_'+Year+'.root','recreate')
hratio_onlywjets.Write()
newtfile.Close()
