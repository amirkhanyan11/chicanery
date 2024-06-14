#include <iostream>


class Person
{

public:

    Person(const std::string& name) : m_name{name} {}

private:

    mutable std::string m_name {};

public:

    void set_name(const std::string& name)
    {
        this->m_name = name;
    }

    const std::string& get_name() const
    {
        return this->m_name;
    }
};


int main()
{
    Person p("muguch");
    std::cout << p.get_name() << std::endl;
    
}