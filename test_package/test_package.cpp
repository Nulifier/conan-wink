#include <wink/slot.hpp>
#include <wink/signal.hpp>

struct Event {
    int a;
}

int main()
{
    wink::slot<void (int)> mySlot;
    wink::signal<wink::slot<void (int)> mySignal;
    wink::event_queue<Event> myEventQueue;
}
