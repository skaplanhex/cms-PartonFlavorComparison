from ROOT import *
#gROOT.SetStyle("Plain")
#SetBatch() makes it so the picture isn't displayed on the screen when saved; this saves lots of time!
gROOT.SetBatch()
gStyle.SetOptStat(11)
c = TCanvas()
c.SetBorderMode(0)
c.SetFillColor(kWhite)
genDict = {'tt_pythia6_plots.root':'pythia6','tt_pythia8_plots.root':'pythia8','tt_sherpa_plots.root':'sherpa','tt_mg_plots.root':'mg','tt_herwig6_pythiastatus_plots.root':'herwig6_pythiastatus','tt_herwig6_herwigstatus_plots.root':'herwig6_herwigstatus'}
binLabelDict = {1:'b',2:'c',3:'d',4:'g',5:"noMatch",6:'s',7:'u'}
numGenDict = {0:'pythia6',1:'pythia8',2:'sherpa',3:'mg',4:'herwig6_pythiastatus',5:'herwig6_herwigstatus'}

bHistos = []
cHistos = []
sHistos = []
noMatchHistos = []
uHistos = []
dHistos = []
gHistos = []
lightHistos = [] #lightHisto = u+d+s+g
flavorHistos = []

bHistosOld = []
cHistosOld = []
sHistosOld = []
noMatchHistosOld = []
uHistosOld = []
dHistosOld = []
gHistosOld = []
lightHistosOld = [] #lightHisto = u+d+s+g
flavorHistosOld = []

c = TCanvas()
for filename in ('tt_pythia6_plots.root','tt_pythia8_plots.root','tt_sherpa_plots.root','tt_mg_plots.root','tt_herwig6_pythiastatus_plots.root','tt_herwig6_herwigstatus_plots.root'):
	f = TFile("oldplotrootfiles/"+filename,"READ")

	histptold = f.Get('analyzerAK5/hPartonFlavorOld_Pt')
	histptnew = f.Get('analyzerAK5/hPartonFlavorNew_Pt')

	histptold.LabelsOption('a','Y')
	histptnew.LabelsOption('a','Y')

	flavHistNew = histptnew.ProjectionY()
	flavHistNew.LabelsOption('a','X') #may not be needed, but I guess it doesn't hurt
	flavHistNew.SetDirectory(0) #don't go out of scope!
	flavHistNew.SetName(genDict[filename]+"_flavordist")
	flavHistNew.GetYaxis().SetRangeUser(0,120000)
	flavorHistos.append(flavHistNew)

	flavHistOld = histptold.ProjectionY()
	flavHistOld.LabelsOption('a','X') #may not be needed, but I guess it doesn't hurt
	flavHistOld.SetDirectory(0)
	flavHistOld.GetYaxis().SetRangeUser(0,120000)
	flavorHistosOld.append(flavHistOld)

	#loop over flavor bins and get pT distribution for each flavor
	for bin in (1,2,3,4,5,6,7):
		projold = histptold.ProjectionX(binLabelDict[bin]+"_pt_old_"+genDict[filename],bin,bin)
		projnew = histptnew.ProjectionX(binLabelDict[bin]+"_pt_new_"+genDict[filename],bin,bin)

		projold.SetTitle("pT Distribution of " + binLabelDict[bin] + " jets " + genDict[filename] + " (old tool)")
		projnew.SetTitle("pT Distribution of " + binLabelDict[bin] + " jets "+ genDict[filename]+" (new tool)")
		projold.GetXaxis().SetTitle('pT (GeV/c)')
		projnew.GetXaxis().SetTitle('pT (GeV/c)')

		projold.GetXaxis().SetRangeUser(0,300)
		projnew.GetXaxis().SetRangeUser(0,300)

		projold.SetDirectory(0)
		projnew.SetDirectory(0)

		if (bin == 1):
			bHistos.append(projnew)
			bHistosOld.append(projold)
		elif (bin == 2):
			cHistos.append(projnew)
			cHistosOld.append(projold)
		elif (bin == 3):
			dHistos.append(projnew)
			dHistosOld.append(projold)
		elif (bin == 4):
			gHistos.append(projnew)
			gHistosOld.append(projold)
		elif (bin == 5):
			noMatchHistos.append(projnew)
			noMatchHistosOld.append(projold)
		elif (bin == 6):
			sHistos.append(projnew)
			sHistosOld.append(projold)
		elif (bin == 7):
			uHistos.append(projnew)
			uHistosOld.append(projold)

#build light histograms
for gen in range(6): #numbers represent generators in order they are looped over above (easy way to get histograms from arrays)

	lightHistoNew = TH1D('light_pt_new_' + numGenDict[gen],"light jet pt",500,0,500)
	lightHistoNew.Add(uHistos[gen],1)
	lightHistoNew.Add(dHistos[gen],1)
	lightHistoNew.Add(sHistos[gen],1)
	lightHistoNew.Add(gHistos[gen],1)
	lightHistos.append(lightHistoNew)

	lightHistoOld = TH1D('light_pt_old_' + numGenDict[gen],"light jet pt",500,0,500)
	lightHistoOld.Add(uHistosOld[gen],1)
	lightHistoOld.Add(dHistosOld[gen],1)
	lightHistoOld.Add(sHistosOld[gen],1)
	lightHistoOld.Add(gHistosOld[gen],1)
	lightHistosOld.append(lightHistoOld)

	if (gen == 0 or gen == 3):
		bHistos[gen].SetLineColor(kBlack)
		cHistos[gen].SetLineColor(kBlack)
		sHistos[gen].SetLineColor(kBlack)
		noMatchHistos[gen].SetLineColor(kBlack)
		uHistos[gen].SetLineColor(kBlack)
		dHistos[gen].SetLineColor(kBlack)
		gHistos[gen].SetLineColor(kBlack)
		lightHistos[gen].SetLineColor(kBlack)

		bHistosOld[gen].SetLineColor(kBlack)
		cHistosOld[gen].SetLineColor(kBlack)
		sHistosOld[gen].SetLineColor(kBlack)
		noMatchHistosOld[gen].SetLineColor(kBlack)
		uHistosOld[gen].SetLineColor(kBlack)
		dHistosOld[gen].SetLineColor(kBlack)
		gHistosOld[gen].SetLineColor(kBlack)
		lightHistosOld[gen].SetLineColor(kBlack)

		flavorHistos[gen].SetLineColor(kBlack)
		flavorHistosOld[gen].SetLineColor(kBlack)
		flavorHistos[gen].SetMarkerColor(kBlack)
		flavorHistosOld[gen].SetMarkerColor(kBlack)
		flavorHistos[gen].SetMarkerStyle(20)
		flavorHistosOld[gen].SetMarkerStyle(20)

	elif (gen == 1):
		bHistos[gen].SetLineColor(kBlue)
		cHistos[gen].SetLineColor(kBlue)
		sHistos[gen].SetLineColor(kBlue)
		noMatchHistos[gen].SetLineColor(kBlue)
		uHistos[gen].SetLineColor(kBlue)
		dHistos[gen].SetLineColor(kBlue)
		gHistos[gen].SetLineColor(kBlue)
		lightHistos[gen].SetLineColor(kBlue)

		bHistosOld[gen].SetLineColor(kBlue)
		cHistosOld[gen].SetLineColor(kBlue)
		sHistosOld[gen].SetLineColor(kBlue)
		noMatchHistosOld[gen].SetLineColor(kBlue)
		uHistosOld[gen].SetLineColor(kBlue)
		dHistosOld[gen].SetLineColor(kBlue)
		gHistosOld[gen].SetLineColor(kBlue)
		lightHistosOld[gen].SetLineColor(kBlue)

		flavorHistos[gen].SetLineColor(kBlue)
		flavorHistosOld[gen].SetLineColor(kBlue)
		flavorHistos[gen].SetMarkerColor(kBlue)
		flavorHistosOld[gen].SetMarkerColor(kBlue)
		flavorHistos[gen].SetMarkerStyle(21)
		flavorHistosOld[gen].SetMarkerStyle(21)

	elif (gen == 4 or gen == 2):
		bHistos[gen].SetLineColor(kRed)
		cHistos[gen].SetLineColor(kRed)
		sHistos[gen].SetLineColor(kRed)
		noMatchHistos[gen].SetLineColor(kRed)
		uHistos[gen].SetLineColor(kRed)
		dHistos[gen].SetLineColor(kRed)
		gHistos[gen].SetLineColor(kRed)
		lightHistos[gen].SetLineColor(kRed)

		bHistosOld[gen].SetLineColor(kRed)
		cHistosOld[gen].SetLineColor(kRed)
		sHistosOld[gen].SetLineColor(kRed)
		noMatchHistosOld[gen].SetLineColor(kRed)
		uHistosOld[gen].SetLineColor(kRed)
		dHistosOld[gen].SetLineColor(kRed)
		gHistosOld[gen].SetLineColor(kRed)
		lightHistosOld[gen].SetLineColor(kRed)

		flavorHistos[gen].SetLineColor(kRed)
		flavorHistosOld[gen].SetLineColor(kRed)
		flavorHistos[gen].SetMarkerColor(kRed)
		flavorHistosOld[gen].SetMarkerColor(kRed)
		flavorHistos[gen].SetMarkerStyle(22)
		flavorHistosOld[gen].SetMarkerStyle(22)

	elif (gen == 5):
		bHistos[gen].SetLineColor(kMagenta)
		cHistos[gen].SetLineColor(kMagenta)
		sHistos[gen].SetLineColor(kMagenta)
		noMatchHistos[gen].SetLineColor(kMagenta)
		uHistos[gen].SetLineColor(kMagenta)
		dHistos[gen].SetLineColor(kMagenta)
		gHistos[gen].SetLineColor(kMagenta)
		lightHistos[gen].SetLineColor(kMagenta)

		bHistosOld[gen].SetLineColor(kMagenta)
		cHistosOld[gen].SetLineColor(kMagenta)
		sHistosOld[gen].SetLineColor(kMagenta)
		noMatchHistosOld[gen].SetLineColor(kMagenta)
		uHistosOld[gen].SetLineColor(kMagenta)
		dHistosOld[gen].SetLineColor(kMagenta)
		gHistosOld[gen].SetLineColor(kMagenta)
		lightHistosOld[gen].SetLineColor(kMagenta)

		flavorHistos[gen].SetLineColor(kMagenta)
		flavorHistosOld[gen].SetLineColor(kMagenta)
		flavorHistos[gen].SetMarkerColor(kMagenta)
		flavorHistosOld[gen].SetMarkerColor(kMagenta)
		flavorHistos[gen].SetMarkerStyle(33)
		flavorHistosOld[gen].SetMarkerStyle(33)

#test
# bHistos[0].Draw()
# bHistos[1].Draw("same")
# legend = TLegend(0.5,0.6,0.79,0.79)
# legend.AddEntry(bHistos[0],"Pythia 6","L")
# legend.AddEntry(bHistos[1],"Pythia 8","L")
# legend.Draw()
# c.SaveAs("test.png")
# c.Clear()

#numGenDict = {0:'pythia6',1:'pythia8',2:'sherpa',3:'mg',4:'herwig6_pythiastatus',5:'herwig6_herwigstatus'}
flavorHistos[0].SetTitle("Jet Parton Flavor")
flavorHistos[0].GetXaxis().SetTitle("Jet Flavor")
flavorHistos[0].GetYaxis().SetTitle("Number Of Jets / Flavor")
flavorHistos[0].GetYaxis().SetTitleOffset(1.4)
flavorHistos[0].Draw()
flavorHistos[0].Draw("sameP0")
flavorHistos[1].Draw("same")
flavorHistos[1].Draw("sameP0")
flavorHistos[4].Draw("same")
flavorHistos[4].Draw("sameP0")
flavorHistos[5].Draw("same")
flavorHistos[5].Draw("sameP0")
legend = TLegend(0.66,0.5,0.9,0.73)
legend.AddEntry(flavorHistos[0],"Pythia 6","LP")
legend.AddEntry(flavorHistos[1],"Pythia 8","LP")
legend.AddEntry(flavorHistos[4],"Herwig 6 (Pythia Status)","LP")
legend.AddEntry(flavorHistos[5],"Herwig 6 (Herwig Status)","LP")
legend.Draw()
c.SaveAs("flavdist_pythiaherwig_nocuts.png")
c.Clear()

# bHistos[2].SetTitle("pT of Jets With Parton Flavor = b")
# bHistos[2].GetXaxis().SetTitle("pT (GeV)")
# bHistos[2].GetYaxis().SetTitle("Number Of Jets / 1 GeV")
# bHistos[2].GetYaxis().SetTitleOffset(1.4)
# bHistos[2].Draw()
# bHistos[3].Draw("same")
# legend = TLegend(0.66,0.5,0.9,0.73)
# legend.AddEntry(bHistos[2],"Sherpa","L")
# legend.AddEntry(bHistos[3],"Madgraph + Pythia 6","L")
# legend.Draw()
# c.SaveAs("bpt_sherpamg_withcuts.png")
# c.Clear()



flavorHistos[2].SetTitle("Jet Parton Flavor")
flavorHistos[2].GetXaxis().SetTitle("Jet Flavor")
flavorHistos[2].GetYaxis().SetTitle("Number Of Jets / Flavor")
flavorHistos[2].GetYaxis().SetTitleOffset(1.4)
flavorHistos[2].Draw()
flavorHistos[2].Draw("sameP0")
flavorHistos[3].Draw("same")
flavorHistos[3].Draw("sameP0")
legend = TLegend(0.66,0.5,0.9,0.73)
legend.AddEntry(flavorHistos[2],"Sherpa","LP")
legend.AddEntry(flavorHistos[3],"Madgraph + Pythia 6","LP")
legend.Draw()
c.SaveAs("flavdist_sherpamg_nocuts.png")
c.Clear()






		# projold.Draw()
		# c.SaveAs(binLabelDict[bin]+"_"+genDict[filename]+"_old_"+"pt.png")
		# c.Clear()

		# projnew.Draw()
		# c.SaveAs(binLabelDict[bin]+"_"+genDict[filename]+"_new_"+"pt.png")
		# c.Clear()
