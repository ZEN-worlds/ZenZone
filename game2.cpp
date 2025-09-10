// main.cpp (very small skeleton)
#include <SFML/Graphics.hpp>
int main(){
  sf::RenderWindow window(sf::VideoMode(800,480),"ZenZone");
  sf::RectangleShape player(sf::Vector2f(20,28));
  player.setFillColor(sf::Color::White);
  player.setPosition(100,100);
  while(window.isOpen()){
    sf::Event e;
    while(window.pollEvent(e)) if(e.type==sf::Event::Closed) window.close();
    // physics, input...
    window.clear(sf::Color(6,18,31));
    window.draw(player);
    window.display();
  }
  return 0;
}

