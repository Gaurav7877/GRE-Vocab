import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
import random

# kivy.require('1.9.0')


class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()
        self.gold_label.text = 'G: ' + str(gold)

    def level_options(self):
        global lvl
        self.ques_label.color = (1, 1, 1, 1)
        self.def1_label.color = (1, 1, 1, 0.9)
        self.def2_label.color = (1, 1, 1, 0.9)
        self.def3_label.color = (1, 1, 1, 0.9)
        self.def4_label.color = (1, 1, 1, 0.9)
        self.start_label.text = 'Start'
        self.ques_label.text = 'Select Level'
        self.def1_label.text = 'Level ' + str(lvl)
        lvl = lvl + 1
        self.def2_label.text = 'Level ' + str(lvl)
        lvl = lvl + 1
        self.def3_label.text = 'Level ' + str(lvl)
        lvl = lvl + 1
        self.def4_label.text = 'Level ' + str(lvl)
        lvl = lvl + 1
        if lvl > 20:
            lvl = 1

    def next_question(self):
        global indicies, lb, ub
        self.def1_label.color = (1, 1, 1, 0.9)
        self.def2_label.color = (1, 1, 1, 0.9)
        self.def3_label.color = (1, 1, 1, 0.9)
        self.def4_label.color = (1, 1, 1, 0.9)
        if ub > len(words):
            ub = len(words) - 1
        quesidx = random.randint(lb, ub)
        ques = words[quesidx]
        indicies = [1, 2, 3, 4]
        ans = []
        ans.append(definitions[quesidx])
        ans.append(definitions[random.randint(lb, ub)])
        ans.append(definitions[random.randint(lb, ub)])
        ans.append(definitions[random.randint(lb, ub)])
        # shuffle function
        for i in range(0, 15):
            idx1 = random.randint(0, 3)
            idx2 = random.randint(0, 3)
            if idx1 == idx2:
                continue
            temp = ans[idx1]
            ans[idx1] = ans[idx2]
            ans[idx2] = temp
            temp = indicies[idx1]
            indicies[idx1] = indicies[idx2]
            indicies[idx2] = temp
        # presenting the question
        self.ques_label.text = ques
        self.def1_label.text = ans[0]
        self.def2_label.text = ans[1]
        self.def3_label.text = ans[2]
        self.def4_label.text = ans[3]
        self.ques_label.color = (1, 1, 1, 1)
        self.gold_label.text = 'G: ' + str(gold)
        self.start_label.text = 'Skip'

    def option1_press(self):
        global indicies, gold, lb, ub
        if self.def1_label.text[:5] == 'Level':
            temp = int(self.def1_label.text[6:])
            lb = (temp - 1) * 50
            ub = temp * 50 - 1
            self.ques_label.text = self.def1_label.text
            return
        if self.ques_label.text == 'Select Best':
            self.best_summon_label.text = self.def1_label.text
            self.best_summon_label.color = self.def1_label.color
            return
        if indicies[0] == 1:
            if self.ques_label.color == [1, 1, 1, 1]:
                gold = gold + 1
            self.next_question()
        else:
            self.def1_label.text = "nooo"
            self.ques_label.color = (1, 0, 0, 1)

    def option2_press(self):
        global indicies, gold, lb, ub
        if self.def2_label.text[:5] == 'Level':
            temp = int(self.def2_label.text[6:])
            lb = (temp - 1) * 50
            ub = temp * 50 - 1
            self.ques_label.text = self.def2_label.text
            return
        if self.ques_label.text == 'Select Best':
            self.best_summon_label.text = self.def2_label.text
            self.best_summon_label.color = self.def2_label.color
            return
        if indicies[1] == 1:
            if self.ques_label.color == [1, 1, 1, 1]:
                gold = gold + 1
            self.next_question()
        else:
            self.def2_label.text = "nooo"
            self.ques_label.color = (1, 0, 0, 1)

    def option3_press(self):
        global indicies, gold, lb, ub
        if self.def3_label.text[:5] == 'Level':
            temp = int(self.def3_label.text[6:])
            lb = (temp - 1) * 50
            ub = temp * 50 - 1
            self.ques_label.text = self.def3_label.text
            return
        if self.ques_label.text == 'Select Best':
            self.best_summon_label.text = self.def3_label.text
            self.best_summon_label.color = self.def3_label.color
            return
        if indicies[2] == 1:
            if self.ques_label.color == [1, 1, 1, 1]:
                gold = gold + 1
            self.next_question()
        else:
            self.def3_label.text = "nooo"
            self.ques_label.color = (1, 0, 0, 1)

    def option4_press(self):
        global indicies, gold, lb, ub
        if self.def4_label.text[:5] == 'Level':
            temp = int(self.def4_label.text[6:])
            lb = (temp - 1) * 50
            ub = temp * 50 - 1
            self.ques_label.text = self.def4_label.text
            return
        if self.ques_label.text == 'Select Best':
            self.best_summon_label.text = self.def4_label.text
            self.best_summon_label.color = self.def4_label.color
            return
        if indicies[3] == 1:
            if self.ques_label.color == [1, 1, 1, 1]:
                gold = gold + 1
            self.next_question()
        else:
            self.def4_label.text = "nooo"
            self.ques_label.color = (1, 0, 0, 1)

    def summon(self):
        global gold, summoned, hype
        if gold < 5:
            return
        rand = random.random()
        if rand < 0.4:
            summoned = str(common[random.randint(0, len(common) - 1)])
        elif rand < 0.7:
            summoned = str(rare[random.randint(0, len(rare) - 1)])
        elif rand < 0.85:
            summoned = str(superrare[random.randint(0, len(superrare) - 1)])
        elif rand < 0.95:
            summoned = str(supersuperrare[random.randint(0, len(supersuperrare) - 1)])
        elif rand < 1.00:
            summoned = str(ultrarare[random.randint(0, len(ultrarare) - 1)])
        gold = gold - 5
        self.gold_label.text = 'G: ' + str(gold)
        self.summon_label.text = summoned
        if summoned not in acquired:
            acquired.append(summoned)
        hype = 0
        self.create_hype()

    def best_summon(self):
        global i, best_list
        self.ques_label.color = (1, 1, 1, 1)
        self.def1_label.color = (1, 1, 1, 0.9)
        self.def2_label.color = (1, 1, 1, 0.9)
        self.def3_label.color = (1, 1, 1, 0.9)
        self.def4_label.color = (1, 1, 1, 0.9)
        if self.best_summon_label.text == '':
            try:
                self.def1_label.text = best_list[i]
                self.color_names(1, self.def1_label.text)
            except:
                self.def1_label.text = '- - - - - - - - - -'
            i = i + 1
            try:
                self.def2_label.text = best_list[i]
                self.color_names(2, self.def2_label.text)
            except:
                self.def2_label.text = '- - - - - - - - - -'
            i = i + 1
            try:
                self.def3_label.text = best_list[i]
                self.color_names(3, self.def3_label.text)
            except:
                self.def3_label.text = '- - - - - - - - - -'
            i = i + 1
            try:
                self.def4_label.text = best_list[i]
                self.color_names(4, self.def4_label.text)
            except:
                self.def4_label.text = '- - - - - - - - - -'
                self.best_summon_label.text = ' '
            i = i + 1
            return
        self.best_summon_label.text = ''
        self.ques_label.text = 'Select Best'
        self.start_label.text = 'Start'
        best_list = []
        best_list = best_list + list(set(acquired) & set(ultrarare))
        best_list = best_list + list(set(acquired) & set(supersuperrare))
        best_list = best_list + list(set(acquired) & set(superrare))
        best_list = best_list + list(set(acquired) & set(rare))
        best_list = best_list + list(set(acquired) & set(common))
        i = 0
        try:
            self.def1_label.text = best_list[i]
            self.color_names(1, self.def1_label.text)
        except:
            self.def1_label.text = '- - - - - - - - - -'
        i = i + 1
        try:
            self.def2_label.text = best_list[i]
            self.color_names(2, self.def2_label.text)
        except:
            self.def2_label.text = '- - - - - - - - - -'
        i = i + 1
        try:
            self.def3_label.text = best_list[i]
            self.color_names(3, self.def3_label.text)
        except:
            self.def3_label.text = '- - - - - - - - - -'
        i = i + 1
        try:
            self.def4_label.text = best_list[i]
            self.color_names(4, self.def4_label.text)
        except:
            self.def4_label.text = '- - - - - - - - - -'
            self.best_summon_label.text = ' '
        i = i + 1

    def color_names(self, num, name):
        if name in common:
            if num == 1:
                self.def1_label.color = (1, 1, 1, 0.9)
            elif num == 2:
                self.def2_label.color = (1, 1, 1, 0.9)
            elif num == 3:
                self.def3_label.color = (1, 1, 1, 0.9)
            elif num == 4:
                self.def4_label.color = (1, 1, 1, 0.9)
        elif name in rare:
            if num == 1:
                self.def1_label.color = (0, 1, 0, 0.9)
            elif num == 2:
                self.def2_label.color = (0, 1, 0, 0.9)
            elif num == 3:
                self.def3_label.color = (0, 1, 0, 0.9)
            elif num == 4:
                self.def4_label.color = (0, 1, 0, 0.9)
        elif name in superrare:
            if num == 1:
                self.def1_label.color = (0.3, 0.3, 1, 0.9)
            elif num == 2:
                self.def2_label.color = (0.3, 0.3, 1, 0.9)
            elif num == 3:
                self.def3_label.color = (0.3, 0.3, 1, 0.9)
            elif num == 4:
                self.def4_label.color = (0.3, 0.3, 1, 0.9)
        elif name in supersuperrare:
            if num == 1:
                self.def1_label.color = (1, 0.2, 0.2, 0.9)
            elif num == 2:
                self.def2_label.color = (1, 0.2, 0.2, 0.9)
            elif num == 3:
                self.def3_label.color = (1, 0.2, 0.2, 0.9)
            elif num == 4:
                self.def4_label.color = (1, 0.2, 0.2, 0.9)
        elif name in ultrarare:
            if num == 1:
                self.def1_label.color = (1, 1, 0, 0.9)
            elif num == 2:
                self.def2_label.color = (1, 1, 0, 0.9)
            elif num == 3:
                self.def3_label.color = (1, 1, 0, 0.9)
            elif num == 4:
                self.def4_label.color = (1, 1, 0, 0.9)

    def create_hype(self):
        global hype
        if hype == -1:
            return
        if summoned in common:
            self.summon_label.text = 'C: ' + summoned
            self.summon_label.color = (1, 1, 1, 0.9)
            hype = -1
            return
        elif hype == 0:
            hype = hype + 1
            self.summon_label.text = 'C: '
            self.summon_label.color = (1, 1, 1, 0.9)
            return

        if summoned in rare:
            self.summon_label.text = 'R: ' + summoned
            self.summon_label.color = (0, 1, 0, 0.9)
            hype = -1
            return
        elif hype == 1:
            hype = hype + 1
            self.summon_label.text = 'R: '
            self.summon_label.color = (0, 1, 0, 0.9)
            return

        if summoned in superrare:
            self.summon_label.text = 'SR: ' + summoned
            self.summon_label.color = (0.3, 0.3, 1, 0.9)
            hype = -1
            return
        elif hype == 2:
            hype = hype + 1
            self.summon_label.text = 'SR: '
            self.summon_label.color = (0.3, 0.3, 1, 0.9)
            return

        if summoned in supersuperrare:
            self.summon_label.text = 'SSR: ' + summoned
            self.summon_label.color = (1, 0.2, 0.2, 0.9)
            hype = -1
            return
        elif hype == 3:
            hype = hype + 1
            self.summon_label.text = 'SSR: '
            self.summon_label.color = (1, 0.2, 0.2, 0.9)
            return

        if summoned in ultrarare:
            self.summon_label.text = 'UR: ' + summoned
            self.summon_label.color = (1, 1, 0, 0.9)
            hype = -1
            return


class PrepGame(App):

    def build(self):
        # Set window size
        w = 90 * 3
        h = 195 * 3
        Config.set('graphics', 'width', str(w))
        Config.set('graphics', 'height', str(h))

        return MyRoot()


# function for reading file and extracting words and definitions
def get_words():
    global ub
    string = "note|a brief written record|board|a stout length of sawn timber|claim|assert or affirm strongly|opportune|suitable or advantageous especially for a particular purpose|weary|physically and mentally fatigued|strain|exert much effort or energy|ally|a friendly nation|extent|the point or degree to which something extends|obvious|easily perceived by the senses or grasped by the mind|prompt|according to schedule or without delay|pitch|the high or low quality of a sound|expend|use up or consume fully|swift|moving very fast|desperate|a person who is frightened and in need of help|manifest|clearly revealed to the mind or the senses or judgment|confine|place limits on|notion|a general inclusive concept|neglect|leave undone or leave out|induce|cause to act in a specified manner|startle|surprise greatly|embrace|squeeze tightly in your arms, usually with fondness|precious|of high worth or cost|vigor|forceful exertion|presume|take to be the case or to be true|profound|situated at or extending to great depth|prudent|marked by sound judgment|stiff|incapable of or resistant to bending|plead|appeal or request earnestly|spell|write or name the letters that comprise the accepted form of|indulge|yield to; give satisfaction to|subsequent|following in time or order|absurd|inconsistent with reason or logic or common sense|strive|attempt by employing effort|peer|look searchingly|contend|compete for something|scattered|lacking orderly continuity|stake|a strong wooden or metal post driven into the ground|agitate|move or cause to move back and forth|pine|a coniferous tree|obscure|not clearly understood or expressed|flatter|praise somewhat dishonestly|steep|having a sharp inclination|console|give moral or emotional strength to|jest|activity characterized by good humor|extensive|large in spatial extent or range or scope or quantity|deprive|take away|concede|give over|conspire|act in agreement and in secret towards a deceitful purpose|proposition|a suggestion offered for acceptance or rejection|discourse|an extended communication dealing with some particular topic|endeavor|attempt by employing effort|disguise|any attire that conceals the wearer's identity|decree|a legally binding command or decision|sway|move back and forth|harbor|a sheltered port where ships can take on or discharge cargo|literal|limited to the explicit meaning of a word or text|substantial|real; having a material or factual existence|stoop|bend one's back forward from the waist on down|frown|a facial expression of dislike or displeasure|sober|not affected by a chemical substance, especially alcohol|vanity|feelings of excessive pride|petition|a formal request that something be submitted to an authority|ingenious|showing inventiveness and skill|quiver|shake with fast, tremulous movements|defiant|boldly resisting authority or an opposing force|perplex|be a mystery or bewildering to|torment|intense feelings of suffering; acute mental or physical pain|vex|disturb, especially by minor irritations|gravity|the force of attraction between all masses in the universe|conspicuous|obvious to the eye or mind|subdue|put down by force or intimidation|redeem|exchange or buy back for money; under threat|indignant|angered at something unjust or wrong|recede|pull back or move away or backward|enchant|cast a spell over someone or something|pluck|pull lightly but sharply|apprehension|fearful expectation or anticipation|extravagant|recklessly wasteful|venerate|regard with feelings of respect and reverence|prolong|lengthen in time; cause to be or last longer|guarded|cautious and reserved|distract|draw someone's attention away from something|reckless|marked by defiant disregard for danger or consequences|exploit|use or manipulate to one's advantage|formidable|extremely impressive in strength or excellence|fraud|intentional deception resulting in injury to another person|forge|create by hammering|linen|a fabric woven with fibers from the flax plant|avert|turn away or aside|confound|be confusing or perplexing to|charter|a document creating an institution and specifying its rights|intrigue|a crafty and involved plot to achieve your ends|defer|yield to another's wish or opinion|diligent|quietly and steadily persevering in detail or exactness|brood|hang over, as of something threatening, dark, or menacing|traitor|a person who says one thing and does another|dazzle|cause to lose clear vision, especially from intense light|brisk|quick and energetic|cower|crouch or curl up|breach|an opening, especially a gap in a dike or fortification|latitude|an imaginary line around the Earth parallel to the equator|denounce|speak out against|attentive|taking heed|benevolent|showing or motivated by sympathy and understanding|conjecture|believe especially on uncertain or tentative grounds|eloquence|powerful and effective language|stray|wander from a direct course or at random|shrill|having or emitting a high-pitched and sharp tone or tones|falter|move hesitatingly, as if about to give way|mend|restore by putting together what is torn or broken|shatter|break into many pieces|disdain|lack of respect accompanied by a feeling of intense dislike|remorse|a feeling of deep regret, usually for some misdeed|dissent|a difference of opinion|loom|a textile machine for weaving yarn into a textile|enlist|join the military|rash|imprudently incurring risk|propriety|correct behavior|plea|a humble request for help from someone in authority|crave|have an appetite or great desire for|concession|the act of yielding|perch|an elevated place serving as a seat|grumble|make complaining remarks or noises under one's breath|fathom|a linear unit of measurement for water depth|proclamation|a formal public statement|defiance|a hostile challenge|levy|impose and collect|assess|estimate the nature, quality, ability or significance of|mirth|great merriment|fret|be agitated or irritated|prodigy|an unusually gifted or intelligent person|ascribe|attribute or credit to|vicious|having the nature of evildoing|venerable|profoundly honored|precipice|a very steep cliff|confidential|given in secret|dwarf|a person who is markedly small|blunder|an embarrassing mistake|cavern|a large cave or a large chamber in a cave|waver|pause or hold back in uncertainty or unwillingness|precipitate|bring about abruptly|slack|not tense or taut|limp|walk impeded by some physical injury|lavish|very generous|censure|harsh criticism or disapproval|discreet|marked by prudence or modesty and wise self-restraint|trample|tread or stomp heavily or roughly|condescend|behave in a patronizing manner|withhold|hold back; refuse to hand over or share|valiant|having or showing heroism or courage|corporal|affecting the body as opposed to the mind or spirit|gorge|a deep ravine, usually with a river running through it|premise|a statement that is held to be true|gravel|rock fragments and pebbles|subside|wear off or die down|adverse|in an opposing direction|caprice|a sudden desire|clumsy|lacking grace in movement or posture|insensible|barely able to be perceived|uphold|stand up for; stick up for; of causes, principles, or ideals|pertinent|being of striking appropriateness|rejoicing|a feeling of great happiness|fervent|characterized by intense emotion|aspiration|a cherished desire|indict|accuse formally of a crime|austere|of a stern or strict bearing or demeanor|invoke|request earnestly; ask for aid or protection|ghastly|shockingly repellent; inspiring horror|exhort|spur on or encourage especially by cheers and shouts|lumber|the wood of trees prepared for use as building material|wary|marked by keen caution and watchful prudence|treacherous|dangerously unstable and unpredictable|conjure|summon into action or bring into existence|affliction|a cause of great suffering and distress|endorse|approve of|judicious|marked by the exercise of common sense in practical matters|detached|no longer connected or joined|placid|calm and free from disturbance|ominous|threatening or foreshadowing evil or tragic developments|spine|the series of vertebrae forming the backbone|contingent|determined by conditions or circumstances that follow|impudent|improperly forward or bold|concur|happen simultaneously|impetuous|characterized by undue haste and lack of thought|articulate|express or state clearly|ordinance|an authoritative rule|annex|attach to|pervade|spread or diffuse through|impede|be a hindrance or obstacle to|censor|a person authorized to suppress unacceptable material|presumption|a premise that is taken for granted|foster|providing nurture though not related by blood or legal ties|prodigious|great in size, force, extent, or degree|admonish|scold or reprimand; take to task|acquiesce|agree or express agreement|complacent|contented to a fault with oneself or one's actions|steadfast|marked by firm determination or resolution; not shakable|usurp|seize and take control without authority|oblivion|the state of being disregarded or forgotten|allegiance|the act of binding yourself to a course of action|pan|shallow container made of metal|atone|turn away from sin or do penitence|smother|deprive of oxygen and prevent from breathing|susceptible|yielding readily to or capable of|vulnerable|capable of being wounded or hurt|shun|avoid and stay away from deliberately|odium|hate coupled with disgust|pebble|a small smooth rounded rock|deference|courteous regard for people's feelings|intricate|having many complexly arranged elements; elaborate|meddle|intrude in other people's affairs or business|approbation|official acceptance or agreement|vindicate|show to be right by providing justification or proof|posture|the arrangement of the body and its limbs|uproar|a state of commotion and noise and confusion|luminous|softly bright or radiant|sinister|wicked, evil, or dishonorable|explicit|precisely and clearly expressed or readily observable|temperate|not extreme|rigor|excessive sternness|insinuate|suggest in an indirect or covert way; give to understand|feign|make believe with the intent to deceive|flirt|talk or behave amorously, without serious intentions|truce|a state of peace agreed to between opponents|imperative|requiring attention or action|impair|make worse or less effective|hamper|prevent the progress or free movement of|curb|the act of restraining power or action or limiting excess|frivolous|not serious in content, attitude, or behavior|deter|turn away from as by fear or persuasion|transgress|act in disregard of laws, rules, contracts, or promises|augment|enlarge or increase|lull|make calm or still|allegation|a formal accusation against somebody|abyss|a bottomless gulf or pit|composure|steadiness of mind under stress|covet|wish, long, or crave for|bleak|unpleasantly cold and damp|heretic|a person whose religious beliefs conflict with church dogma|controversial|marked by or capable of causing disagreement|sip|drink in sips|consternation|sudden shock or dismay that causes confusion|metaphysics|the philosophical study of being and knowing|stark|severely simple|frenzy|state of violent mental agitation|odious|extremely repulsive or unpleasant|din|a loud, harsh, or strident noise|evoke|call forth, as an emotion, feeling, or response|prone|having a tendency|imperious|having or showing arrogant superiority|overhaul|make repairs, renovations, revisions or adjustments to|apparition|a ghostly appearing figure|lucid|transparently clear; easily understandable|coherent|marked by an orderly and consistent relation of parts|stipulate|make an express demand or provision in an agreement|drought|a shortage of rainfall|martial|suggesting war or military life|wile|the use of tricks to deceive someone|recourse|act of turning to for assistance|outset|the time at which something is supposed to begin|ludicrous|inviting ridicule|infuse|fill, as with a certain quality|conceit|the trait of being unduly vain|dubious|fraught with uncertainty or doubt|feud|a bitter quarrel between two parties|dangle|hang freely|skeptical|marked by or given to doubt|decorum|propriety in manners and conduct|tangible|perceptible by the senses, especially the sense of touch|cant|a slope in the turn of a road or track|covert|secret or hidden|avarice|reprehensible acquisitiveness; insatiable desire for wealth|jeer|laugh at with contempt and derision|devoid|completely wanting or lacking|mitigate|lessen or to try to lessen the seriousness or extent of|wardrobe|a piece of furniture that provides storage space for clothes|arbitrate|act between parties with a view to reconciling differences|deft|skillful in physical movements; especially of the hands|consign|give over to another for care or safekeeping|dispel|cause to separate and go in different directions|disinterested|unaffected by concern for one's own welfare|epithet|descriptive word or phrase|supplicate|ask for humbly or earnestly, as in prayer|deluge|a heavy rain|plaintive|expressing sorrow|tapestry|a wall hanging of heavy fabric with pictorial designs|furtive|secret and sly|obliterate|remove completely from recognition or memory|bog|wet spongy ground of decomposing vegetation|vigilance|the process of paying close and continuous attention|veritable|not counterfeit or copied|dwindle|become smaller or lose substance|succumb|give in, as to overwhelming force, influence, or pressure|prerogative|a right reserved exclusively by a person or group|sordid|foul and run-down and repulsive|wan|pale, as of a person's complexion|fawn|a young deer|perpetuate|cause to continue or prevail|drone|make a monotonous low dull sound|ambiguous|having more than one possible meaning|parasite|an animal or plant that lives in or on a host|tout|advertise in strongly positive terms|commentator|an expert who observes and remarks on something|oblique|slanting or inclined in direction or course or position|encroach|advance beyond the usual limit|ascetic|someone who practices self denial as a spiritual discipline|prodigal|recklessly wasteful|ensign|a person who holds a commissioned rank in the U.S. Navy|recompense|make payment to|improvise|manage in a makeshift way; do with whatever is at hand|enigma|something that baffles understanding and cannot be explained|flinch|draw back, as with fear or pain|placate|cause to be more favorably inclined|intact|undamaged in any way|whimsical|determined by chance or impulse rather than by necessity|pestilence|any epidemic disease with a high death rate|dedication|complete and wholehearted fidelity|drawl|a slow speech pattern with prolonged vowels|overture|orchestral music at the beginning of an opera or musical|gird|bind with something round or circular|inquisitive|given to questioning|precarious|not secure; beset with difficulties|peremptory|putting an end to all debate or action|ponderous|having great mass and weight and unwieldiness|efface|remove by or as if by rubbing or erasing|invert|turn inside out or upside down|captor|a person who entraps and holds someone else|incongruous|lacking in harmony or compatibility or appropriateness|arable|capable of being farmed productively|fallacy|a misconception resulting from incorrect reasoning|vogue|a current state of general acceptance and use|mercenary|a person hired to fight for another country than their own|coerce|cause to do through pressure or necessity|discomfit|cause to lose one's composure|obtrude|push to thrust outward|lizard|relatively long-bodied reptile with legs and a tapering tail|audacious|disposed to venture or take risks|arduous|characterized by effort to the point of exhaustion|profuse|produced or growing in extreme abundance|reciprocal|concerning each of two or more persons or things|tremor|an involuntary vibration, as if from illness or fear|stint|supply sparingly and with restricted quantities|provocation|a means of arousing or stirring to action|embellish|make more attractive, as by adding ornament or color|affable|diffusing warmth and friendliness|tentative|hesitant or lacking confidence; unsettled in mind or opinion|stifled|held in check with difficulty|pillage|steal goods; take as spoils|varnish|a coating that provides a hard, lustrous finish to a surface|vehemence|intensity or forcefulness of expression|obsolete|no longer in use|ingenuous|lacking in sophistication or worldliness|corroborate|give evidence for|lucrative|producing a sizeable profit|vindictive|disposed to seek revenge or intended for revenge|bolster|support and strengthen|gaudy|tastelessly showy|prune|cultivate, tend, and cut back the growth of|ostensible|appearing as such but not necessarily so|omnipotent|having unlimited power|protracted|relatively long in duration|stigma|a symbol of disgrace or infamy|pedant|a person who is preoccupied with rules and learning|craven|lacking even the rudiments of courage; abjectly fearful|plumb|exactly vertical|droll|comical in an odd or whimsical manner|plod|walk heavily and firmly, as when weary, or through mud|reticent|reluctant to draw attention to yourself|benign|kind in disposition or manner|affluent|having an abundant supply of money or possessions of value|propensity|a natural inclination|topple|fall down, as if collapsing|grazing|the act of grazing|dupe|fool or hoax|pernicious|exceedingly harmful|espouse|choose and follow a theory, idea, policy, etc.|intrepid|invulnerable to fear or intimidation|consensus|agreement in the judgment reached by a group as a whole|jovial|full of or showing high-spirited merriment|denunciation|a public act of condemnation|engrossed|giving or marked by complete attention to|extant|still in existence; not extinct or destroyed or lost|elicit|call forth, as an emotion, feeling, or response|guile|shrewdness as demonstrated by being skilled in deception|perennial|lasting an indefinitely long time|tacit|implied by or inferred from actions or statements|mediocre|moderate to inferior in quality|jeopardy|a source of danger|plaintiff|a person who brings an action in a court of law|fervor|feelings of great warmth and intensity|blithe|carefree and happy and lighthearted|docile|easily handled or managed|indigenous|originating where it is found|mistrust|regard with suspicion|exemplify|be characteristic of|swindle|(offensive) deprive of by deceit|harangue|a loud bombastic declamation expressed with strong emotion|eradicate|destroy completely, as if down to the roots|sate|fill to contentment|cessation|a stopping|practitioner|someone who carries out a learned profession|illicit|contrary to accepted morality or convention|obese|excessively large|impunity|exemption from punishment or loss|pedestrian|a person who travels by foot|flop|fall loosely|flounder|move clumsily or struggle to move, as in mud or water|malign|speak unfavorably about|ostentatious|intended to attract notice and impress others|averse|strongly opposed|nausea|the state that precedes vomiting|epistle|a specially long, formal letter|alacrity|liveliness and eagerness|impediment|something immaterial that interferes with action or progress|auspicious|indicating favorable circumstances and good luck|precipitous|extremely steep|divest|take away possessions from someone|conscript|enroll into service compulsorily|espy|catch sight of|strut|walk in a proud, confident way|bizarre|conspicuously or grossly unconventional or unusual|occult|supernatural forces and events and beings collectively|inundate|fill or cover completely, usually with water|diffident|showing modest reserve|supplant|take the place or move into the position of|forgery|criminal falsification by making or altering an instrument|conflagration|a very intense and uncontrolled fire|implacable|incapable of being appeased or pacified|hapless|unfortunate and deserving pity|deposition|the act of putting something somewhere|perfidy|an act of deliberate betrayal|doleful|filled with or evoking sadness|pique|call forth, as an emotion, feeling, or response|squander|spend thoughtlessly; throw away|elusive|skillful at evading capture|fickle|liable to sudden unpredictable change|profligate|unrestrained by convention or morality|leash|restraint consisting of a rope used to restrain an animal|encumber|hold back, impede, or weigh down|goad|stab or urge on as if with a pointed stick|petulant|easily irritated or annoyed|balk|refuse to proceed or comply|engender|call forth|expiate|make amends for|exigent|demanding immediate attention|banter|light teasing repartee|delineate|represented accurately or precisely|moat|ditch dug as a fortification and usually filled with water|quack|the sound made by a duck|extol|praise, glorify, or honor|fidget|move restlessly|antipathy|a feeling of intense dislike|emissary|someone sent to represent another's interests|pathology|the branch of medical science that studies diseases|obnoxious|causing disapproval or protest|garner|assemble or get together|aptitude|inherent ability|preclude|make impossible, especially beforehand|tarnish|make or become dirty or dull, as by exposure to air|foreclosure|proceedings initiated to repossess the collateral for a loan|grill|a framework of metal bars used as a partition or a grate|appraise|consider in a comprehensive way|precedence|status established in order of importance or urgency|vagrant|a wanderer with no established residence or means of support|obtrusive|sticking out; protruding|stockade|fortification consisting of a fence set firmly for defense|confrontation|discord resulting from a clash of ideas or opinions|concoct|make something by mixing|burlesque|a theatrical entertainment of broad and earthy humor|impassive|having or revealing little emotion or sensibility|erratic|liable to sudden unpredictable change|tamp|press down tightly|reinstate|bring back into original existence, function, or position|aver|declare or affirm solemnly and formally as true|astute|marked by practical hardheaded intelligence|voluptuous|displaying luxury and furnishing gratification to the senses|onslaught|an offensive against an enemy|leaven|a substance used to produce fermentation in dough|zenith|the highest point of something|credulity|tendency to believe readily|invigorate|give life or energy to|obsession|an unhealthy and compulsive preoccupation with something|skiff|a small boat propelled by oars or by sails or by a motor|philanthropist|someone who makes charitable donations|veracity|unwillingness to tell lies|prosaic|lacking wit or imagination|descry|catch sight of|imbue|spread or diffuse through|caustic|capable of destroying or eating away by chemical action|reverberate|ring or echo with sound|bask|expose oneself to warmth and light, as for relaxation|decorous|characterized by propriety and dignity and good taste|imbibe|take in liquids|hallucinate|have illusions; perceive what is not actually there|ineffable|defying expression or description|nocturnal|belonging to or active during the night|demur|politely refuse or take exception to|presumptuous|going beyond what is appropriate, permitted, or courteous|adept|having or showing knowledge and skill and aptitude|buttress|a support usually of stone or brick|grudging|petty or reluctant in giving or spending|pungent|strong and sharp to the sense of taste or smell|dormant|inactive but capable of becoming active|magnanimity|nobility and generosity of spirit|exuberant|joyously unrestrained|impregnable|incapable of being attacked or tampered with|somber|serious and gloomy in character|dislodge|remove or force from a position previously occupied|avid|marked by active interest and enthusiasm|shirk|avoid one's assigned duties|inadvertent|happening by chance or unexpectedly or unintentionally|propitiate|make peace with|exemplary|worthy of imitation|salvage|rescuing a ship or its crew from a shipwreck or a fire|drab|a dull greyish to yellowish or light olive brown|annotate|add explanatory notes to or supply with critical comments|annul|cancel officially|opaque|not transmitting or reflecting light or radiant energy|coy|affectedly shy especially in a playful or provocative way|narcotic|a drug that produces numbness or stupor|apprise|inform somebody of something|fanatical|marked by excessive enthusiasm for a cause or idea|verdant|characterized by abundance of vegetation and green foliage|disparate|fundamentally different or distinct in quality or kind|dogmatic|pertaining to a code of beliefs accepted as authoritative|digress|wander from a direct or straight course|morose|showing a brooding ill humor|belie|be in contradiction with|levee|an embankment built to prevent a river from overflowing|forestall|keep from happening or arising; make impossible|rampant|occurring or increasing in an unrestrained way|flaunt|display proudly|divulge|make known to the public information previously kept secret|laudable|worthy of high praise|lethargy|inactivity; showing an unusual lack of energy|pith|spongelike central cylinder of the stems of flowering plants|elucidate|make clear and comprehensible|nonchalant|marked by casual unconcern or indifference|convoke|call together|dissemble|behave unnaturally or affectedly|invective|abusive language used to express blame or censure|brittle|having little elasticity|provocative|serving or tending to excite or stimulate|epitome|a standard or typical example|despicable|morally reprehensible|flimsy|a thin strong lightweight translucent paper|oscillate|move or swing from side to side regularly|squalid|foul and run-down and repulsive|conciliatory|making or willing to make concessions|felon|someone who has been legally convicted of a crime|crease|an angular indentation made by folding|hypocritical|professing feelings or virtues one does not have|malevolent|wishing or appearing to wish evil to others|maverick|someone who exhibits independence in thought and action|florid|elaborately or excessively ornamented|tenable|based on sound reasoning or evidence|taciturn|habitually reserved and uncommunicative|amalgamate|bring or combine together or with something else|piquant|having an agreeably pungent taste|taut|pulled or drawn tight|indelible|not able to be forgotten, removed, or erased|facetious|cleverly amusing in tone|spurious|plausible but false|immutable|not subject or susceptible to change or variation|lustrous|reflecting light|efficacious|giving the power to produce an intended result|flippant|showing an inappropriate lack of seriousness|gloat|dwell on with satisfaction|disprove|show to be false|obsequious|attempting to win favor from influential people by flattery|mosaic|design made of small pieces of colored stone or glass|distend|cause to expand as if by internal pressure|glib|artfully persuasive in speech|clot|a lump of material formed from the content of a liquid|pucker|gather something into small wrinkles or folds|laconic|brief and to the point|insipid|lacking interest or significance or impact|impromptu|with little or no preparation or forethought|incursion|the act of entering some territory or domain|loll|be lazy or idle|meager|deficient in amount or quality or extent|tantalize|harass with persistent teasing or baiting|adulterate|make impure by adding a foreign or inferior substance|exorbitant|greatly exceeding bounds of reason or moderation|cajole|influence or urge by gentle urging, caressing, or flattering|entrenched|dug in|unequivocal|admitting of no doubt or misunderstanding|vacillate|be undecided about something|conducive|tending to bring about; being partly responsible for|obviate|do away with|mettle|the courage to carry on|ameliorate|make better|complaisant|showing a cheerful willingness to do favors for others|opus|a musical work that has been created|specious|plausible but false|recluse|one who lives in solitude|boor|a crude uncouth ill-bred person lacking refinement|dabble|bob under so as to feed off the bottom of a body of water|obtuse|of an angle, between 90 and 180 degrees|vagary|an unexpected and inexplicable change in something|incipient|only partly in existence; imperfectly formed|obdurate|stubbornly persistent in wrongdoing|grovel|show submission or fear|refractory|stubbornly resistant to authority or control|foment|try to stir up|foment|try to stir up|assuage|provide physical relief, as from pain|adamant|very hard native crystalline carbon valued as a gem|quarantine|isolation to prevent the spread of infectious disease|pundit|an expert who publicly gives opinions via mass media|predilection|a predisposition in favor of something|perfunctory|hasty and without attention to detail; not thorough|preamble|a preliminary introduction, as to a statute or constitution|officious|intrusive in a meddling or offensive manner|evict|expel or eject without recourse to legal process|disparity|inequality or difference in some respect|ornate|marked by complexity and richness of detail|culpable|deserving blame or censure as being wrong or injurious|plummet|drop sharply|oligarchy|a political system governed by a few people|viable|capable of life or normal growth and development|dearth|an insufficient quantity or number|qualm|uneasiness about the fitness of an action|cognizance|the state or act of having knowledge of|imposture|pretending to be another person|insignia|a badge worn to show official position|lope|run easily|trepidation|a feeling of alarm or dread|infiltrate|pass through an enemy line in a military conflict|dispassionate|unaffected by strong emotion or prejudice|flout|treat with contemptuous disregard|panegyric|formally expressing praise|gainsay|take exception to|obituary|a notice of someone's death|deprivation|the disadvantage that results from losing something|garrulous|full of trivial conversation|slur|utter indistinctly|precursor|something indicating the approach of something or someone|jocular|characterized by jokes and good humor|obeisance|bending the head or body in reverence or submission|obligatory|required by compulsion or convention|overt|open and observable; not secret or hidden|untoward|not in keeping with accepted standards of what is proper|idiosyncrasy|a behavioral attribute peculiar to an individual|fervid|characterized by intense emotion|heretical|departing from accepted beliefs or standards|impervious|not admitting of passage or capable of being affected|perfidious|tending to betray|platitude|a trite or obvious remark|sloppy|lacking neatness or order|sporadic|recurring in scattered or unpredictable instances|meticulous|marked by precise accordance with details|attenuate|become weaker, in strength, value, or magnitude|polemic|a verbal or written attack, especially of a belief or dogma|holster|a sheath for carrying a handgun|disburse|expend, as from a fund|penury|a state of extreme poverty or destitution|flamboyant|tending to attract attention; marked by ostentatious display|mollify|cause to be more favorably inclined|mundane|found in the ordinary course of events|incorrigible|impervious to correction by punishment|foible|a minor weakness or peculiarity in someone's character|gist|the central meaning or theme of a speech or literary work|baleful|threatening or foreshadowing evil or tragic developments|orifice|an opening, especially one that opens into a bodily cavity|contentious|showing an inclination to disagree|subpoena|a writ issued to compel the attendance of a witness|fluffy|like down or as soft as down|dirge|a song or hymn of mourning as a memorial to a dead person|amenable|disposed or willing to comply|adulate|flatter in an obsequious manner|inextricable|incapable of being disentangled or untied|enervate|weaken physically, mentally, or morally|wheedle|influence or urge by gentle urging, caressing, or flattering|ranger|an official responsible for managing an area of forest|omniscient|knowing, seeing, or understanding everything|untenable|incapable of being defended or justified|ephemeral|anything short-lived, as an insect that lives only for a day|insular|relating to or characteristic of or situated on an island|eclectic|selecting what seems best of various styles or ideas|obelisk|a stone pillar tapering towards a pyramidal top|contrite|feeling or expressing pain or sorrow|decry|express strong disapproval of|welter|a confused multitude of things|voracious|devouring or craving food in great quantities|torpor|a state of motor and mental inactivity|enthral|hold spellbound|distraught|deeply agitated especially from emotion|savant|a learned person|effrontery|audacious behavior that you have no right to|hoax|something intended to deceive|tepid|moderately warm|dampen|lessen in force or effect|eschew|avoid and stay away from deliberately|quibble|evade the truth of a point by raising irrelevant objections|recant|formally reject or disavow a formerly held belief|crockery|ceramic dishes used for serving food|guileless|innocent and free of deceit|rationale|an explanation of the fundamental reasons|abstruse|difficult to understand|opulence|wealth as evidenced by sumptuous living|spendthrift|someone who spends money freely or wastefully|anachronism|locating something at a time when it couldn't have existed|redoubtable|inspiring fear|anomalous|deviating from the general or common order or type|shuck|material consisting of seed coverings and small pieces of stem or leaves that have been separated from the seeds|commensurate|corresponding in size or degree or extent|adulation|exaggerated flattery or praise|torpid|in a condition of biological rest or suspended animation|quaff|swallow hurriedly or greedily or in one draught|ramification|a consequence, especially one that causes complications|libertine|unrestrained by convention or morality|fluke|a stroke of luck|irate|feeling or showing extreme anger|tirade|a speech of violent denunciation|egregious|conspicuously and outrageously bad or reprehensible|idolatrous|relating to or practicing idolatry|irascible|quickly aroused to anger|cogent|powerfully persuasive|sedulous|marked by care and persistent effort|aggrandize|embellish; increase the scope, power, or importance of|inflammable|easily ignited|evanescent|short-lived; tending to vanish or disappear|asperity|harshness of manner|leviathan|the largest or most massive thing of its kind|bombast|pompous or pretentious talk or writing|circumspect|careful to consider potential consequences and avoid risk|pristine|immaculately clean and unused|inimical|tending to obstruct or cause harm|paragon|a perfect embodiment of a concept|gouge|an impression in a surface, as made by a blow|exonerate|pronounce not guilty of criminal charges|lugubrious|excessively mournful|oratorio|a musical composition for voices and orchestra|ogle|stare or look at, especially with amorous intentions|probity|complete and confirmed integrity|putrefy|decay with an offensive smell|fledgling|young bird that has just become capable of flying|bogus|fraudulent; having a misleading appearance|incidence|the relative frequency of occurrence of something|banal|repeated too often; overfamiliar through overuse|rescind|cancel officially|debilitate|make weak|pedantry|an ostentatious and inappropriate display of learning|omnipresent|existing everywhere at once|odorous|having a characteristic aroma|fallacious|containing or based on incorrect reasoning|esoteric|understandable only by an enlightened inner circle|foolhardy|marked by defiant disregard for danger or consequences|nondescript|lacking distinct or individual characteristics|gregarious|temperamentally seeking and enjoying the company of others|inured|made tough by habitual exposure|opprobrium|a state of extreme dishonor|forthright|directly and without evasion; not roundabout|encomium|a formal expression of praise|antiseptic|thoroughly clean and free of disease-causing organisms|nefarious|extremely wicked|orientation|the act of determining one's position|phlegmatic|showing little emotion|fortuitous|lucky; occurring by happy chance|abeyance|temporary cessation or suspension|exacerbate|make worse|orthography|representing the sounds of a language by written symbols|overwrought|deeply agitated especially from emotion|onerous|burdensome or difficult to endure|burgeon|grow and flourish|gossamer|a gauze fabric with an extremely fine texture|simper|smile in an insincere, unnatural, or coy way|iniquitous|characterized by injustice or wickedness|prodigality|the trait of spending extravagantly|inept|generally incompetent and ineffectual|hyperbole|extravagant exaggeration|aqueous|similar to or containing or dissolved in water|vilify|spread negative information about|atrophy|a decrease in size of an organ caused by disease or disuse|innocuous|not injurious to physical or mental health|stigmatize|condemn or openly brand as disgraceful|trenchant|having keenness and forcefulness and penetration in thought|debacle|a sudden and complete disaster|opiate|a narcotic drug|petulance|an irritable feeling|lasso|a long noosed rope used to catch animals|penchant|a strong liking or preference|pugnacious|ready and able to resort to force or violence|rarefy|lessen the density or solidity of|vituperate|spread negative information about|ornithology|the branch of zoology that studies birds|collusion|secret agreement|mace|a ceremonial staff carried as a symbol of office|blandishment|flattery intended to persuade|noisome|causing or able to cause nausea|loquacious|full of trivial conversation|euphemism|an inoffensive expression substituted for an offensive one|erudite|having or showing profound knowledge|vertigo|a reeling sensation; a feeling that you are about to fall|baneful|evil or sinister|outgrowth|the gradual beginning or coming forth|flustered|thrown into a state of agitated confusion|dilettante|an amateur engaging in an activity without serious intention|pusillanimous|lacking in courage, strength, and resolution|ingrained|deeply rooted; firmly fixed or held|shunt|a conductor diverting a fraction of current from a device|proclivity|a natural inclination|mercurial|liable to sudden unpredictable change|optimum|most desirable possible under a restriction|hackneyed|repeated too often; overfamiliar through overuse|catalyst|substance that initiates or accelerates a chemical reaction|abscond|run away, often taking something or somebody along|equivocate|be deliberately ambiguous or unclear|prevaricate|be deliberately ambiguous or unclear|recalcitrant|stubbornly resistant to authority or control|loafer|a person who is idle and does no work|inopportune|not suitable for a purpose|quash|declare invalid|astringent|tending to draw together or constrict soft organic tissue|castigate|inflict severe punishment on|fulminate|cause to explode violently and with loud noise|profundity|the quality of being physically deep|impugn|attack as false or wrong|sketchy|giving only major points; lacking completeness|plethora|extreme excess|obloquy|state of disgrace resulting from public abuse|striate|marked with stripes|dumbfound|be a mystery or bewildering to|lethargic|deficient in alertness or activity|chary|characterized by great caution|volubility|the quality of being facile in speech and writing|refurbish|improve the appearance or functionality of|aspersion|a disparaging remark|predisposition|an inclination to interpret statements in a particular way|extempore|with little or no preparation or forethought|prescience|the power to foresee the future|abstemious|marked by temperance in indulgence|nadir|the lowest point of anything|fracas|a noisy quarrel|iconoclast|someone who attacks cherished ideas or institutions|neuralgia|acute spasmodic pain along the course of one or more nerves|saturnine|bitter or scornful|ebullient|joyously unrestrained|exculpate|pronounce not guilty of criminal charges|zealot|a fervent and even militant proponent of something|ambivalent|uncertain or unable to decide about what course to follow|oblation|the act of contributing to the funds of a church or charity|recondite|difficult to understand|jamb|a vertical side piece of a door or window frame|zephyr|a slight wind|paucity|an insufficient quantity or number|offal|viscera and trimmings of a butchered animal|antediluvian|of or relating to the period before the biblical flood|overweening|presumptuously arrogant|circumlocution|an indirect way of expressing something|preen|clean with one's bill|tyro|someone new to a field or activity|gavel|a small mallet used by a presiding officer or a judge|felicitate|express congratulations|diatribe|thunderous verbal attack|heterodox|characterized by departure from accepted standards|lackluster|not having brilliance or vitality|squelch|suppress or crush completely|conifer|a type of tree or shrub bearing cones|obstreperous|noisily and stubbornly defiant|gaffe|a socially awkward or tactless act|obliquity|the quality of being deliberately vague or deceptive|opprobrious|expressing offensive reproach|apocryphal|being of questionable authenticity|veracious|habitually speaking the truth|bellicose|having or showing a ready disposition to fight|agog|highly excited|misanthrope|someone who dislikes people in general|stickler|someone who insists on something|equivocation|intentional vagueness or ambiguity|olfactory|of or relating to the sense of smell|euphoria|a feeling of great elation|ostracism|the act of excluding someone from society by general consent|herbaceous|characteristic of a nonwoody herb or plant part|quenching|the act of extinguishing; causing to stop burning|impecunious|not having enough money to pay for necessities|chicanery|the use of tricks to deceive someone|gullible|naive and easily deceived or tricked|inauspicious|boding ill|odoriferous|emitting a smell, especially an unpleasant smell|demote|assign to a lower position; reduce in rank|disrobe|get undressed|disabuse|free somebody from an erroneous belief|martinet|someone who demands exact conformity to rules and forms|quintessential|representing the perfect example of a class or quality|opportunist|a person who places expediency above principle|desiccate|lacking vitality or spirit; lifeless|intransigent|impervious to pleas, persuasion, requests, or reason|barefaced|with no effort to conceal|quiescence|a state of quiet but possibly temporary)inaction|onus|a burdensome or difficult concern|misnomer|an incorrect or unsuitable name|orison|reverent petition to a deity|insatiate|impossible to satisfy|ornithologist|a scientist who studies birds|ethos|the distinctive spirit of a culture or an era|minuscule|very small|feckless|generally incompetent and ineffectual|interregnum|the time between two reigns or governments|suborn|incite to commit a crime or an evil deed|posit|take as a given; assume as a postulate or axiom|ambrosial|worthy of the gods|opalescent|having a play of lustrous rainbow colors|oculist|a person skilled in testing for defects of vision|cadge|obtain or seek to obtain by wheedling|turpitude|a corrupt or depraved or degenerate act or practice|tangential|of superficial relevance if any|gauche|lacking social polish, poise, or refinement|peccadillo|a petty misdeed|improvidence|a lack of prudence, care, or foresight|discrete|constituting a separate entity or part|ostracize|expel from a community or group|inchoate|only partly in existence; imperfectly formed|obstetrician|a physician specializing in childbirth|outmoded|no longer in fashion|omnivorous|feeding on both plants and animals|convoluted|highly complex or intricate|macerate|soften and cause to disintegrate as a result|foppish|overly concerned with extreme elegance in dress and manner|obsidian|glass formed by the cooling of lava without crystallization|mendacious|given to lying|rotundity|the roundness of a 3-dimensional object|optician|a worker who makes glasses for remedying defects of vision|objurgate|censure severely|oaf|an awkward, foolish person|bilk|cheat somebody out of what is due, especially money|objurgation|rebuking a person harshly|egalitarian|favoring social equality|adumbrate|describe roughly or give the main points or summary of|finicky|fussy, especially about details|obfuscate|make obscure or unclear|vituperative|marked by harshly abusive criticism|molt|cast off hair, skin, horn, or feathers|dichotomy|a classification into two opposed parts or subclasses|mettlesome|having a proud, courageous, and unbroken spirit|truculence|stubborn and defiant aggressiveness|calisthenics|light exercises designed to promote general fitness|ossified|set in a rigidly conventional pattern of behavior or beliefs|aberrant|markedly different from an accepted norm|syncopated|stressing a normally weak beat|epistemology|the philosophical theory of knowledge|misogynist|a misanthrope who dislikes women in particular|emollient|a substance with a soothing effect when applied to the skin|disassemble|take apart|homeopathy|a method of treating disease with small amounts of remedies that, in large amounts in healthy people, produce symptoms similar to those being treated|quotidian|found in the ordinary course of events|aesthete|one who professes great sensitivity to the beauty of art|mollycoddle|treat with excessive indulgence|congruent|corresponding in character or kind|nonplused|filled with bewilderment|conflate|mix together different elements|offertory|the offerings of the congregation at a religious service|ligneous|consisting of or resembling wood|aphoristic|terse and witty and like a maxim|optometrist|a person skilled in testing for defects of vision|analgesic|capable of relieving pain|malingerer|someone shirking duty by feigning illness or incapacity|onomatopoeia|using words that imitate the sound they denote|orotund|overly formal and pompous in style|coagulant|an agent that produces coagulation|limerick|a humorous rhymed verse form of five lines|parquetry|a patterned wood inlay used to cover a floor|polymath|a person of great and varied learning|faddish|intensely fashionable or popular for a short time|malapropism|misuse of a word by confusion with one that sounds similar"
    slices = string.split('|')
    a = 0
    while True:
        try:
            words.append(slices[a])
            definitions.append(slices[a + 1])
            a = a + 2
        except:
            break
    ub = len(words)


# function to read file and extract characters can later
def get_characters():
    commonstring = "Grisha Jeager|Carla Jeager|Keith Shadis|Hannes|Recovery Girl|Lunch Rush|Yuga Aoyama|Mashirao Ojiro|Koji Koda|Hanta Sero|Mezo Shoji|Minoru Mineta|Mirajane Strauss|Cana Alberona|Sister Lily|Marx Francois|Sekke Vronzazza|Ichigo Shikai|Naruto Academy|Naruto 1 Tail Cloak|Saske Academy|Saske Academy|Sakura Academy|Luffy East Blue|Zoro East Blue|Sanji East Blue|Ussop East Blue|Nami East Blue|Chopper Base"
    rarestring = "Historia Reiss|Connie Springer|Sasha Blouse|Jean Kirstein|Krusta Lenz|Ymir|Thirteen|Hound Dog|Power Loader|Mina Ashido|Tsuyu Asui|Ochaco Uraraka|Kyoka Jiro|Toru Hagakure|Momo Yaoyorozu|Mei Hatsume|Eri|Happy|Carla|Panther Lily|Levy McGarden|Klaus Lunettes|Gordon Agrippa|Grey House|Charmy Pappitson|Gauche Adlai|Ichigo Bankai|Naruto Bone Cloak|Saske 2 Tomoe|Saske Stage 1 Curse|Kakashi Anbu|Luffy Jet|Robin Base|Franky Base|Brook Base|Nami Clima Tact"
    superrarestring = "Eren Yeager|Mikasa Akkerman|Armin Arlert|Reiner Braun|Annie Leonhart|Bertolt Hoover|Kenny Ackermann|Nezu (Principal)|Present Mic|Clmentoss|Snipe|Ectoplasm|Vlad King|Best Jeanist|Ryukyu|Edgeshot|Gang Orca|Mt. Lady|Tenya Ida|Denki Kaminari|Eijiro Kirishima|Fumikage Tokoyami|Mirio Togata|Nejire Hado|Tamaki Amajiki|Himiko Toga|Lucy Heartfilia|Vendy Marvell|Juvia Lockser|Mimosa Vermillion|Noelle Silvia|Nero|Luck Voltia|Magna Swing|Vanessa Enoteca|Finral Roulacase|Leopold Vermillion|Kaito|Kahono|Ichigo Hollow|Naruto 9 Tails Partial|Saske 3 Tomoe|Saske Stage 2 Curse|Sakura Creation Rebirth|Copy Ninja Kakashi|Luffy Giant|Zoro Black Blade|Black Leg Sanji|Ussop Sogeking|Franky Swole"
    supersuperrarestring = "Cart Titan|Female Titan|Colossus Titan|Hange Zoe|Erwin Smith|Zeke Jeager|All Might|Midnight|Endeavor|Hawks|Fat Gum|Mirko|Gran Torino|Izuku Midoriya|Kitsuki Bakugo|Shoto Todoroki|Overhaul|Spinner|Mr. Compress|Lady Nagant|Natsu Dragneel|Gray Fullbuster|Erza Scarlet|Gajeel Redfox|Makarov Dreyar|Laxus Dreyar|Gildarts|Evergreen|Loki|Asta|Yuno|Kaito|Kahono|Charlotte Roselei|Rill Boismortier|William Vangeance|Licht|Fana|Rhya|Ichigo Fullbring|Ichigo Vasto Lorde|Naruto Kurama Mode|Saske Eternal Mangekyo Sharingan|Sakura Sozo Saisei|Kakashi Mangekyou Sharingan|Luffy Bounce Man|Luffy Tank Man|Luffy Snake Man|Zoro Asura|Sanji Germa 66|God Ussop|Nami Zeus Tact|Chopper Monster Point|Robin Demon Mode|General Franky|Soul King Brook"
    ultrararestring = "Attack Titan|Armored Titan|Beast Titan|Jaw Titan|War Hammer Titan|Founding Titan|Levi Akkerman|Eraser Head|One For All|All For One|Tomura Shigaraki|Gigantomachia|Dabi|Twice|Julius Novachorno|Yami Sukehiro|Fuegoleon Vermillion|Mereoleona Vermillion|Ichigo Mugetsu|Naruto Sage Of 6 Paths|Saske Rinnegan Sage Of 6 Paths|Saske Indra Mode|Perfect Susano Kakashi|Luffy Sun God Nika"

    a = 0
    slices1 = commonstring.split('|')
    while True:
        try:
            common.append(slices1[a])
            a = a + 1
        except:
            a = 0
            break

    slices2 = rarestring.split('|')
    while True:
        try:
            rare.append(slices2[a])
            a = a + 1
        except:
            a = 0
            break

    slices3 = superrarestring.split('|')
    while True:
        try:
            superrare.append(slices3[a])
            a = a + 1
        except:
            a = 0
            break

    slices4 = supersuperrarestring.split('|')
    while True:
        try:
            supersuperrare.append(slices4[a])
            a = a + 1
        except:
            a = 0
            break

    slices5 = ultrararestring.split('|')
    while True:
        try:
            ultrarare.append(slices5[a])
            a = a + 1
        except:
            a = 0
            break


# initializing the arrays
words = []
definitions = []
acquired = []
best_list = []
i = 0
indicies = [0, 0, 0, 0]
gold = 50
lvl = 1
lb = 0
ub = 0   # updated in get_words func
hype = 0
summoned = ''

common = []
rare = []
superrare = []
supersuperrare = []
ultrarare = []


# calling functions
get_words()
get_characters()

# main driver code
prepGame = PrepGame()
prepGame.run()
