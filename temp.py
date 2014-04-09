from ROOT import *
#gROOT.SetStyle("Plain")
#SetBatch() makes it so the picture isn't displayed on the screen when saved; this saves lots of time!
gROOT.SetBatch()
gStyle.SetOptStat(0)
c = TCanvas()
c.SetBorderMode(0)
c.SetFillColor(kWhite)
c = TCanvas()
l1 = TLatex()
l1.SetTextAlign(12);
l1.SetTextSize(0.045);
l1.SetNDC();
filep6 = TFile("pythia6plots.root","READ")
filep8 = TFile("pythia8plots.root","READ")
fileh6 = TFile("herwig6plots.root","READ")

fileDict = {1:"Pythia6",2:"Pythia8",3:"Herwig6"}
genDict = {1:"Pythia 6",2:"Pythia 8",3:"Herwig 6"}

counter = 0
#see fileDict for relation between counter and hadronizer
for filename in (filep6,filep8,fileh6):
	counter += 1
	numBHadrons = filename.Get("analyzerAK5/hNumBHadrons")
	numBHadronsKeep = filename.Get("analyzerAK5Keep/hNumBHadrons")
	numBHadronsPlusKeepPlus = filename.Get("analyzerAK5PlusKeepPlus/hNumBHadrons")
	numBHadronsPlusKeepPlusPlus = filename.Get("analyzerAK5PlusKeepPlusPlus/hNumBHadrons")

	numCHadrons = filename.Get("analyzerAK5/hNumCHadrons")
	numCHadronsKeep = filename.Get("analyzerAK5Keep/hNumCHadrons")
	numCHadronsPlusKeepPlus = filename.Get("analyzerAK5PlusKeepPlus/hNumCHadrons")
	numCHadronsPlusKeepPlusPlus = filename.Get("analyzerAK5PlusKeepPlusPlus/hNumCHadrons")

	numPartons = filename.Get("analyzerAK5/hNumPartons")
	numPartonsKeep = filename.Get("analyzerAK5Keep/hNumPartons")
	numPartonsPlusKeepPlus = filename.Get("analyzerAK5PlusKeepPlus/hNumPartons")
	numPartonsPlusKeepPlusPlus = filename.Get("analyzerAK5PlusKeepPlusPlus/hNumPartons")

	numLeptons = filename.Get("analyzerAK5/hNumLeptons")
	numLeptonsKeep = filename.Get("analyzerAK5Keep/hNumLeptons")
	numLeptonsPlusKeepPlus = filename.Get("analyzerAK5PlusKeepPlus/hNumLeptons")
	numLeptonsPlusKeepPlusPlus = filename.Get("analyzerAK5PlusKeepPlusPlus/hNumLeptons")

	partonFlavorNew = filename.Get("analyzerAK5/hPartonFlavorNew")
	partonFlavorNewKeep = filename.Get("analyzerAK5Keep/hPartonFlavorNew")
	partonFlavorNewPlusKeepPlus = filename.Get("analyzerAK5PlusKeepPlus/hPartonFlavorNew")
	partonFlavorNewPlusKeepPlusPlus = filename.Get("analyzerAK5PlusKeepPlusPlus/hPartonFlavorNew")

	#change line colors and styles
	histCounter = 0
	for hist in (numBHadrons,numCHadrons,numPartons,numLeptons,partonFlavorNew):
		histCounter += 1
		hist.SetTitle("") #should never see title in any comparison plot
		hist.SetLineColor(kBlack)
		hist.SetLineWidth(2)
		hist.GetXaxis().SetTitleSize(0.045)
		hist.GetYaxis().SetTitleSize(0.045)
		hist.GetXaxis().SetTitleFont(42)
		hist.GetYaxis().SetTitleFont(42)
		hist.GetYaxis().SetTitle("Number of Events")
		#hist.GetYaxis().SetTitleOffset(1.2)
		if (histCounter != 3):
			numBins = hist.GetNbinsX()
			hist.GetXaxis().SetNdivisions(numBins)

	for hist in (numBHadronsKeep,numCHadronsKeep,numPartonsKeep,numLeptonsKeep,partonFlavorNewKeep):
		hist.SetLineColor(kBlue)
		hist.SetLineStyle(3)
		hist.SetLineWidth(2)

	for hist in (numBHadronsPlusKeepPlus,numCHadronsPlusKeepPlus,numPartonsPlusKeepPlus,numLeptonsPlusKeepPlus,partonFlavorNewPlusKeepPlus):
		hist.SetLineColor(kMagenta)
		hist.SetLineStyle(6)
		hist.SetLineWidth(2)

	for hist in (numBHadronsPlusKeepPlusPlus,numCHadronsPlusKeepPlusPlus,numPartonsPlusKeepPlusPlus,numLeptonsPlusKeepPlusPlus,partonFlavorNewPlusKeepPlusPlus):
		hist.SetLineColor(kRed)
		hist.SetLineStyle(8)
		hist.SetLineWidth(2)

	numBHadrons.GetXaxis().SetTitle("B Hadron Multiplicity")
	numBHadrons.Draw()
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	numBHadronsKeep.Draw("same")
	numBHadronsPlusKeepPlus.Draw("same")
	numBHadronsPlusKeepPlusPlus.Draw("same")
	legend = TLegend(0.57,0.5,0.90,0.78)
	legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}")
	legend.AddEntry(numBHadrons,"All GenParticles","L")
	legend.AddEntry(numBHadronsKeep,"Pruned GenParticles (keep)","L")
	legend.AddEntry(numBHadronsPlusKeepPlus,"Pruned GenParticles (+keep+)","L")
	legend.AddEntry(numBHadronsPlusKeepPlusPlus,"Pruned GenParticles (+keep++)","L")
	legend.SetBorderSize(0)
	legend.SetFillColor(kWhite)
	legend.Draw()
	c.SaveAs(fileDict[counter]+"bhadronnumber.png")
	c.Clear()

	numCHadrons.GetXaxis().SetTitle("Charm Hadron Multiplicity")
	numCHadrons.Draw()
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	l1.SetTextSize(0.040);
	numCHadronsKeep.Draw("same")
	numCHadronsPlusKeepPlus.Draw("same")
	numCHadronsPlusKeepPlusPlus.Draw("same")
	legend = TLegend(0.57,0.5,0.90,0.78)
	legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}")
	legend.AddEntry(numCHadrons,"All GenParticles","L")
	legend.AddEntry(numCHadronsKeep,"Pruned GenParticles (keep)","L")
	legend.AddEntry(numCHadronsPlusKeepPlus,"Pruned GenParticles (+keep+)","L")
	legend.AddEntry(numCHadronsPlusKeepPlusPlus,"Pruned GenParticles (+keep++)","L")
	legend.SetBorderSize(0)
	legend.SetFillColor(kWhite)
	legend.Draw()
	c.SaveAs(fileDict[counter]+"chadronnumber.png")
	c.Clear()

	numPartons.GetXaxis().SetTitle("Parton Multiplicity")
	numPartons.Draw()
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	numPartonsKeep.Draw("same")
	numPartonsPlusKeepPlus.Draw("same")
	numPartonsPlusKeepPlusPlus.Draw("same")
	legend = TLegend(0.57,0.5,0.90,0.78)
	legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}")
	legend.AddEntry(numPartons,"All GenParticles","L")
	legend.AddEntry(numPartonsKeep,"Pruned GenParticles (keep)","L")
	legend.AddEntry(numPartonsPlusKeepPlus,"Pruned GenParticles (+keep+)","L")
	legend.AddEntry(numPartonsPlusKeepPlusPlus,"Pruned GenParticles (+keep++)","L")
	legend.SetBorderSize(0)
	legend.SetFillColor(kWhite)
	legend.Draw()
	c.SaveAs(fileDict[counter]+"partonnumber.png")
	c.Clear()

	numLeptons.GetXaxis().SetTitle("Lepton Multiplicity")
	numLeptons.Draw()
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	numLeptonsKeep.Draw("same")
	numLeptonsPlusKeepPlus.Draw("same")
	numLeptonsPlusKeepPlusPlus.Draw("same")
	legend = TLegend(0.57,0.5,0.90,0.78)
	legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}")
	legend.AddEntry(numLeptons,"All GenParticles","L")
	legend.AddEntry(numLeptonsKeep,"Pruned GenParticles (keep)","L")
	legend.AddEntry(numLeptonsPlusKeepPlus,"Pruned GenParticles (+keep+)","L")
	legend.AddEntry(numLeptonsPlusKeepPlusPlus,"Pruned GenParticles (+keep++)","L")
	legend.SetBorderSize(0)
	legend.SetFillColor(kWhite)
	legend.Draw()
	c.SaveAs(fileDict[counter]+"leptonnumber.png")
	c.Clear()

	partonFlavorNew.GetXaxis().SetTitle("Jet Parton Flavor")
	partonFlavorNew.GetYaxis().SetTitle("Number of Jets / Flavor")
	partonFlavorNew.Draw()
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	partonFlavorNewKeep.Draw("same")
	partonFlavorNewPlusKeepPlus.Draw("same")
	partonFlavorNewPlusKeepPlusPlus.Draw("same")
	legend = TLegend(0.57,0.5,0.90,0.78)
	legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}")
	legend.AddEntry(partonFlavorNew,"All GenParticles","L")
	legend.AddEntry(partonFlavorNewKeep,"Pruned GenParticles (keep)","L")
	legend.AddEntry(partonFlavorNewPlusKeepPlus,"Pruned GenParticles (+keep+)","L")
	legend.AddEntry(partonFlavorNewPlusKeepPlusPlus,"Pruned GenParticles (+keep++)","L")
	legend.SetBorderSize(0)
	legend.SetFillColor(kWhite)
	legend.Draw()
	c.SaveAs(fileDict[counter]+"jetflavor.png")
	c.Clear()

filep6pt = TFile("pythia6_ptcomparison_plots.root","READ")
filep8pt = TFile("pythia8_ptcomparison_plots.root","READ")
fileh6pt = TFile("herwig6_ptcomparison_plots.root","READ")

counter = 0
for filename in (filep6pt,filep8pt,fileh6pt):
	counter += 1

	flavpt0 = filename.Get("analyzerAK5Pt0/hPartonFlavorNew")
	flavpt5 = filename.Get("analyzerAK5Pt5/hPartonFlavorNew")
	flavpt10 = filename.Get("analyzerAK5Pt10/hPartonFlavorNew")
	flavpt15 = filename.Get("analyzerAK5Pt15/hPartonFlavorNew")

	flavpt0.SetTitle("") #should never see title in any comparison plot
	flavpt0.SetLineColor(kBlack)
	flavpt0.SetLineWidth(2)
	flavpt0.GetXaxis().SetTitleSize(0.045)
	flavpt0.GetYaxis().SetTitleSize(0.045)
	flavpt0.GetXaxis().SetTitleFont(42)
	flavpt0.GetYaxis().SetTitleFont(42)
	flavpt0.GetXaxis().SetTitle("Jet Parton Flavor")
	flavpt0.GetYaxis().SetTitle("Number of Jets / Flavor")
	flavpt0.GetYaxis().SetTitleOffset(1.1)

	flavpt0.SetLineColor(kBlack)
	flavpt5.SetLineColor(kMagenta)
	flavpt10.SetLineColor(kBlue)
	flavpt15.SetLineColor(kRed)

	flavpt5.SetLineStyle(3)
	flavpt10.SetLineStyle(6)
	flavpt15.SetLineStyle(8)

	flavpt0.SetLineWidth(2)
	flavpt5.SetLineWidth(2)
	flavpt10.SetLineWidth(2)
	flavpt10.SetLineWidth(2)

	flavpt0.Draw()
	flavpt5.Draw("same")
	flavpt10.Draw("same")
	flavpt15.Draw("same")
	l1.SetTextSize(0.045);
	l1.DrawLatex(0.14,0.92, "CMS Simulation Preliminary      #sqrt{s} = 8 TeV")
	if (counter != 2): #if not pythia 8
		legend = TLegend(0.57,0.5,0.90,0.78)
		legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}, Varied Cuts On Light Parton pT")
		legend.AddEntry(flavpt0,"Pruned GenParticles (no cut)","L")
		legend.AddEntry(flavpt5,"Pruned GenParticles (pT > 5 GeV)","L")
		legend.AddEntry(flavpt10,"Pruned GenParticles (pT > 10 GeV)","L")
		legend.AddEntry(flavpt15,"Pruned GenParticles (pT > 15 GeV)","L")
		legend.SetBorderSize(0)
		legend.SetFillColor(kWhite)
		legend.Draw()
		c.SaveAs(fileDict[counter]+"ptcomparison.png")
		c.Clear()
	else: #if pythia 8, need to move legend over in x to not overlap!
		legend = TLegend(0.69,0.45,0.94,0.83)
		legend.SetHeader(genDict[counter]+" t#kern[-1.0]{#bar{t}}, Varied Cuts On Light Parton pT")
		legend.AddEntry(flavpt0,"Pruned GenParticles (no cut)","L")
		legend.AddEntry(flavpt5,"Pruned GenParticles (pT > 5 GeV)","L")
		legend.AddEntry(flavpt10,"Pruned GenParticles (pT > 10 GeV)","L")
		legend.AddEntry(flavpt15,"Pruned GenParticles (pT > 15 GeV)","L")
		legend.SetBorderSize(0)
		legend.SetFillColor(kWhite)
		legend.Draw()
		c.SaveAs(fileDict[counter]+"ptcomparison.png")
		c.Clear()