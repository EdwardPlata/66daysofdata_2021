provider "aws" {
  region = "us-east-1"
  alias = "east"
}

resource "aws_instance" "ss-instance" {
  ami           = "ami-047a51fa27710816e" 
  instance_type = "t3.micro"
  user_data = "${file("userdata.sh")}"
  tags = {
    Name = "Simple Stock App Front End"
  }
}
