from argparse import ArgumentParser as ap
from cowsay import meow
import pyttsx3

engine = pyttsx3.init()

parser = ap(description="Meow like a cat")
parser.add_argument("-n", "--number" , default=1, help="number of times to meow", type=int)
parser.add_argument("-w", "--word", default="meow", help="word/sentence to speak out, -n number or times")
args = parser.parse_args()

word = f"{args.word}\n"
num = int(args.number)

p = word * num

meow(p)
engine.say(p)
engine.runAndWait()
